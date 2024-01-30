import unittest

import armored.catalogs as catalogs


class TestBaseTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_base_table_init(self):
        t = catalogs.BaseTbl(
            name="foo",
            schemas=[catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )


class TestTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_table_init(self):
        t = catalogs.Tbl(
            name="foo",
            schemas=[catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertEqual(t.pk, catalogs.Pk())
        self.assertListEqual(t.fk, [])

        t = catalogs.Tbl(
            name="foo", schemas=[{"name": "foo", "dtype": "varchar( 100 )"}]
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"max_length": 100, "type": "varchar"},
                        "fk": {},
                        "name": "foo",
                        "nullable": True,
                        "pk": False,
                        "unique": False,
                    }
                ],
                "pk": {"columns": [], "name": None},
                "fk": [],
            },
        )

        t = catalogs.Tbl(
            name="foo",
            schemas=[{"name": "foo", "dtype": "varchar( 100 ) primary key"}],
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"max_length": 100, "type": "varchar"},
                        "fk": {},
                        "name": "foo",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    }
                ],
                "pk": {"columns": ["foo"], "name": "foo_pk"},
                "fk": [],
            },
        )
