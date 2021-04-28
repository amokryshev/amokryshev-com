import json
import hashlib
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.management import call_command
from django.test.testcases import LiveServerThread
from django.db import connections
from selenium import webdriver
from .errors import AnimatedPageScenarioImproperlyConfigured


def pers_utf_hash(val):
    """The simple md5 hash without session salt"""

    return int(hashlib.md5(val.encode('utf-8')).hexdigest(), 16)


class FunctionalAnimatedPageTest(StaticLiveServerTestCase):
    """The abstract class for providing setup of selenium framework for all similar testcases of web pages"""

    class Meta:
        abstract = True

    @classmethod
    def setUpClass(cls):
        super(FunctionalAnimatedPageTest, cls).setUpClass()
        cls.selenium = webdriver.Chrome('./chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(FunctionalAnimatedPageTest, cls).tearDownClass()


class AnimatedPageTestScenarioAbstract:
    """The abstract ancestor for the descriptors that provide test scenario for animated pages. The scenario
     gets page_parts dict with XPATH queries to chosen html tags, gets it outerHTML and count hashes,
     next it is doing things, described in _endpoints of certain TestFunc class, depends on concrete Scenario"""
    errors = []
    fields = {}

    class Meta:
        abstract = True

    def __set_name__(self, owner, name):
        for required_field in self.fields:
            if not hasattr(owner, required_field):
                self.errors.append('There isnt required field - {}'.format(required_field))

            elif not type(getattr(owner, required_field)).__name__ in self.fields[required_field]:
                self.errors.append('The required field has wrong type - {}'.
                              format(type(getattr(owner, required_field)).__name__))

            elif not getattr(owner, required_field):
                self.errors.append('The required field - {} is empty'.format(required_field))

            elif required_field == 'page_parts':
                page_p = getattr(owner, required_field)
                for key in page_p:
                    if not isinstance(page_p[key], list):
                        self.errors.append('The page_parts field {0} has wrong type - {1}'.
                                      format(key, type(page_p[key]).__name__))

        if self.errors:
            raise AnimatedPageScenarioImproperlyConfigured(self.errors)

    def __get__(self, instance, owner):
        pass


class AnimatedPageTestScenario(AnimatedPageTestScenarioAbstract):
    """The descriptor for standard animated page test function. The scenario
     gets page_parts dict with XPATH queries to chosen html tags, gets it outerHTML and count hashes,
     next it will doing few django assertions. The descriptor require the owner class to implement fields,
     specified in the AnimatedPageTestScenario.fields attribute."""
    fields = {
        'fixtures': ['list'],
        'references': ['list'],
        'page_parts': ['dict'],
        'snapshots_density': ['int', 'float', ],
        'snapshots_count': ['int'],
    }

    def __get__(self, instance, owner):
        return AnimatedPageTestFunc(owner, instance)


class AnimatedPageGaugeGeneratingScenario(AnimatedPageTestScenarioAbstract):
    """The descriptor for generation gauge of animated page. The scenario
     gets page_parts dict with XPATH queries to chosen html tags, gets it outerHTML and count hashes,
     next stores it to self._new_page_parts, repeats the procedure count of times
     that specified in _instance.snapshots_iter and return final result. The descriptor require of the owner
     class to implement fields, specified in the self.fields attribute."""
    fields = {
        'fixtures': ['list'],
        'references': ['list'],
        'page_parts': ['dict'],
        'snapshots_iter': ['int'],
        'snapshots_density': ['int', 'float', ],
        'snapshots_count': ['int'],
        'connection_alias': ['str'],
        'verbosity': ['int'],
        'host': ['str'],
        'port': ['int'],
    }

    def __get__(self, instance, owner):
        owner.live_server_url = 'http://{0}:{1}'.format(owner.host, owner.port)
        return AnimatedPageGaugeGenFunc(owner, instance)


class AnimatedPageTestFuncAbstract:
    """The abstract class, implements functional to gets page_parts dict with XPATH queries to chosen html tags,
    gets it outerHTML and count hashes, next it is doing things, described in _endpoints of certain TestFunc
    class, depends on concrete Scenario"""

    class Meta:
        abstract = True

    def __init__(self, owner, instance):
        self._owner = owner
        self._instance = instance

    def __call__(self, *args, **kwargs):
        for key in self._instance.references:
            self._response_status_endpoint(uri=key)
            self._owner.selenium.get('{0}{1}'.format(self._instance.live_server_url, key))
            self._owner.selenium.execute_script('for (let i=1; i<10000; i++) {window.scroll(0, i/2)};')
            time.sleep(20)

            for i in range(self._instance.snapshots_count):
                for part in self._instance.page_parts:
                    part_hash = pers_utf_hash(self._owner.selenium.find_element_by_xpath(part).
                                              get_attribute('outerHTML'))
                    self._page_part_action_endpoint(p_hash=part_hash, p_part=part,
                                                    p_content = self._owner.selenium.find_element_by_xpath(part)
                                                    .get_attribute('outerHTML'))
                time.sleep(self._instance.snapshots_density)

            self._final_action_endpoint()

    def _response_status_endpoint(self, *args, **kwargs):
        pass

    def _page_part_action_endpoint(self, *args, **kwargs):
        pass

    def _final_action_endpoint(self, *args, **kwargs):
        pass


class AnimatedPageTestFunc(AnimatedPageTestFuncAbstract):
    """The class, implements functional to gets page_parts dict with XPATH queries to chosen html tags,
        gets it outerHTML and count hashes, next it will doing few django assertions, specified in the _endpoints."""

    def _response_status_endpoint(self, *args, **kwargs):
        response = self._instance.client.get(kwargs['uri'])
        self._instance.assertEqual(response.status_code, 200)

    def _page_part_action_endpoint(self, *args, **kwargs):
        self._instance.assertTrue(kwargs['p_hash'] in self._instance.page_parts[kwargs['p_part']],
                                  msg='There is no {0} in valid hashes of part {1},\n {2}'.
                                  format(kwargs['p_hash'], kwargs['p_part'], kwargs['p_content']))

    def _final_action_endpoint(self, *args, **kwargs):
        self._instance.assertEqual(self._owner.selenium.
                                   execute_script('return document.errorObj.getErrors();'), [])


class AnimatedPageGaugeGenFunc(AnimatedPageTestFuncAbstract):
    """The class, implements functional to gets page_parts dict with XPATH queries to chosen html tags,
    gets it outerHTML and count hashes, next stores it to self._new_page_parts, repeats the procedure
    count of times that specified in _instance.snapshots_iter and return final result. """

    def server_thread_start(self):
        try:
            conn = connections[self._instance.connection_alias]
            conn.creation.create_test_db(self._instance.verbosity, autoclobber=False, keepdb=False,
                                         serialize=conn.settings_dict['TEST'].get('SERIALIZE', True))
            conn.inc_thread_sharing()
            self._instance.connections_override[conn.alias] = conn
            if self._instance.fixtures:
                call_command('loaddata', *self._instance.fixtures,
                             **{'verbosity': self._instance.verbosity, 'database': conn.alias})

            self._instance.server_thread = LiveServerThread(self._instance.host, StaticFilesHandler,
                                                             self._instance.connections_override,
                                                             self._instance.port)
            self._instance.server_thread.daemon = True
            self._instance.server_thread.start()
            self._instance.server_thread.is_ready.wait()

            if self._instance.server_thread.error:
                self.server_thread_stop()
                raise self._instance.server_thread.error

        except Exception as e:
            print(e)
            self.server_thread_stop()

    def server_thread_stop(self):
        self._instance.server_thread.terminate()
        for conn in self._instance.connections_override.values():
            conn.dec_thread_sharing()
            conn.close()

    def __call__(self, *args, **kwargs):
        try:
            self.server_thread_start()
            self._new_page_parts = dict()
            self._owner.selenium = webdriver.Chrome('./chromedriver')
            for i in range(self._instance.snapshots_iter):
                super().__call__()
            return self.result()
        finally:
            self._owner.selenium.quit()
            self.server_thread_stop()

    def _page_part_action_endpoint(self, *args, **kwargs):
        if not kwargs['p_part'] in self._new_page_parts:
            self._new_page_parts.update({kwargs['p_part']: set()})
        self._new_page_parts[kwargs['p_part']].add(kwargs['p_hash'])

    def result(self, *args, **kwargs):
        brand_new_page_parts = dict()
        for key, value in self._new_page_parts.items():
            brand_new_page_parts.update({key: list(value)})
        return brand_new_page_parts


class AnimatedPageGaugeGenerator:
    """The technical class, required for generating gauge, because the inheritor of django Command
    generate the error when is added there an attribute with descriptor"""

    fixtures = ['initial-data.json']
    references = ['/en/', '/ru/', ]
    page_parts = json.loads(open('mainsite/fixtures/index_page_snapshot.json').read())
    snapshots_iter = 10
    snapshots_density = 0.5
    snapshots_count = 120
    connection_alias = 'default'
    connections_override = dict()
    verbosity = 2
    host = '127.0.0.1'
    port = 8090
    GaugeGenerator = AnimatedPageGaugeGeneratingScenario()

    def run(self):
        return self.GaugeGenerator()
