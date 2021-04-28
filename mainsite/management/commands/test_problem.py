import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.test.testcases import LiveServerThread
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.management import call_command


class Command(BaseCommand):
    help = '''
        test command, should be deleted in the future
    '''


    def handle(self, *args, **options):
        try:
            conn = connections['default']
            conn.creation.create_test_db(2, autoclobber=False, keepdb=False,
                                         serialize=conn.settings_dict['TEST'].get('SERIALIZE', True))
            conn.inc_thread_sharing()
            self.connections_override = {}
            self.connections_override[conn.alias] = conn
            fixt = ['mainsite/fixtures/initial-data.json']
            call_command('loaddata', *fixt,
                         **{'verbosity': 2, 'database': conn.alias})

            self.server_thread = LiveServerThread('127.0.0.1', StaticFilesHandler,
                                                            self.connections_override,
                                                            8090)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.server_thread.is_ready.wait()

            if self.server_thread.error:
                self.server_thread.terminate()
                for conn in self.connections_override.values():
                    conn.dec_thread_sharing()
                    conn.close()
                raise self.server_thread.error

            time.sleep(120)

        except Exception as e:
            print(e)
            self.server_thread.terminate()
            for conn in self.connections_override.values():
                conn.dec_thread_sharing()
                conn.close()

