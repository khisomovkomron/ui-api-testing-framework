import pymysql
from api.src.utilities.credentialsUtility import CredentialsUtility
from api.src.configs.hosts_config import DB_HOST
import logging as logger
import os


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, f"Environment variable 'WP_HOST' must be set"

        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set"

        if self.machine == 'docket' and self.wp_host == 'local':
            raise Exception(f"Cannot run test in docker if WP_HOST=local")

        self.env = os.environ.get('ENV', 'test')

        self.host = DB_HOST[self.machine][self.env]['host']
        self.socket = DB_HOST[self.machine][self.env]['socket']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):

        if self.wp_host == 'local':
            connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                         password=self.creds['db_password'], port=self.port)
        elif self.wp_host == 'ammps':
            connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                         password=self.creds['db_password'], port=self.port)
        else:
            raise Exception("Unknown WP_HOST.")
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass
