from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = '''
        The command for creating database within the process of deploying docker containers
    '''

    def handle(self, *args, **options):
        try:
            default_conn = connections['default']
            conn = connections['adm']
            curs = conn.cursor()
            curs.execute("SELECT datname FROM pg_database")
            flag = True
            for db_name in curs.fetchall():
                if db_name[0] == default_conn.settings_dict['NAME']:
                    flag = False
            if flag:
                curs.execute('CREATE DATABASE {}'.format(default_conn.settings_dict['NAME']))

        except Exception as e:
            print(e)
            conn.close()
