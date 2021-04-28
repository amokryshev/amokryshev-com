import os
import json
from django.core.management.base import BaseCommand
from amokryshev.utils import AnimatedPageGaugeGenerator, AnimatedPageScenarioImproperlyConfigured


class Command(BaseCommand):
    help = '''
The command makes file with gauge for the custom functional of testing pages, animated through CSS and JS.
The code and docs of the functional placed in amokryshev.utils.animated_pages_test_tools.py
The Examples:
gauge -f "initial-data.json" -r "/ru" "/en" -p "mainsite/fixtures/index_page_snapshot.json" -v 2 -si 20 -sd 0.1 -sc 400 
gauge -f "initial-data.json" -r "/ru/articles/lorem_ipsum_43/" "/en/articles/lorem_ipsum_46/" -p "mainsite/fixtures/article_page_snapshot.json" -v 2 -si 20 -sd 0.1 -sc 400 
    '''
    GaugeGenerator = AnimatedPageGaugeGenerator()

    parameters = [
        'fixtures',
        'references',
        'page_parts',
        'snapshots_iter',
        'snapshots_density',
        'snapshots_count',
        'connection_alias',
        'verbosity',
        'host',
        'port',
    ]

    def handle(self, *args, **options):
        for param in self.parameters:
            if options[param]:
                setattr(self.GaugeGenerator, param, options[param])
        try:
            if os.path.isfile(self.GaugeGenerator.page_parts):
                gauge_file = open(self.GaugeGenerator.page_parts, "r+")
                print('The {} file has been opened successful!'.format(self.GaugeGenerator.page_parts))
                self.GaugeGenerator.page_parts = json.loads(gauge_file.read())
            else:
                raise AnimatedPageScenarioImproperlyConfigured("Incorrect value in the self.GaugeGenerator.page_parts!")
            gauge_file.truncate(0)
            gauge_file.seek(0)
            gauge_file.write(json.dumps(self.GaugeGenerator.run()))
            print('The file {} has been saved successful!'.format(gauge_file.name))

        except (OSError, IOError) as e:
            print('Something goes wrong when processing Page_parts file: {}'.format(e))

        finally:
            gauge_file.close()
            print('The file has been closed, process completed!')

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--fixtures',
            nargs='+',
            action='store',
            default='initial-data.json',
            help='Fixtures with data for test environment of the page',
            required=True
        )
        parser.add_argument(
            '-r',
            '--references',
            nargs='+',
            action='store',
            help='The list of URNs, that should be tested',
            required=True
        )
        parser.add_argument(
            '-p',
            '--page_parts',
            action='store',
            help='The path to page_parts json',
            required=True
        )
        parser.add_argument(
            '-si',
            '--snapshots_iter',
            type=int,
            action='store',
            help='The count of iteration for snapshots that should be taken from the page (one snapshot per N seconds)',
            required=True
        )
        parser.add_argument(
            '-sd',
            '--snapshots_density',
            type=float,
            action='store',
            help='The density of snapshots that should be  taken from the page (one snapshot per N seconds)',
            required=True
        )
        parser.add_argument(
            '-sc',
            '--snapshots_count',
            type=int,
            action='store',
            help='The count of snapshots that should be taken from the page',
            required=True
        )
        parser.add_argument(
            '-ca',
            '--connection_alias',
            action='store',
            help='The URL of the test server',
            required=False
        )
        parser.add_argument(
            '-ht',
            '--host',
            action='store',
            help='The URL of the test server',
            required=False
        )
        parser.add_argument(
            '-pt',
            '--port',
            type=int,
            action='store',
            help='The port of the test server',
            required=False
        )
