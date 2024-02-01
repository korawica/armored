import unittest

import armored.conn as conn


class TestDBConn(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_db_conn_from_url(self):
        t = conn.DBConn.from_url(
            url=(
                "postgres+psycopg://demo:P@ssw0rd@localhost:5432/db"
                "?echo=True&timeout=10"
            )
        )
        self.assertEqual("postgres+psycopg", t.driver)

        t = conn.DBConn.from_url(
            url="postgres+psycopg://demo:P@ssw0rd@localhost:5432/postgres"
        )
        self.assertEqual("P%40ssw0rd", t.pwd.get_secret_value())
