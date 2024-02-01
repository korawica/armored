import unittest

import armored.dataset as ds


class TestBaseTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_base_table_init(self):
        t = ds.BaseTbl(
            name="foo",
            schemas=[ds.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [ds.Col(name="foo", dtype="varchar( 10 )")],
        )


class TestTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_table_init(self):
        t = ds.Tbl(
            name="foo",
            schemas=[ds.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [ds.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertEqual(t.pk, ds.Pk(of="foo"))
        self.assertListEqual(t.fk, [])

        t = ds.Tbl(
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
                "pk": {"cols": [], "of": "foo"},
                "fk": [],
            },
        )

        t = ds.Tbl(
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
                "pk": {"cols": ["foo"], "of": "foo"},
                "fk": [],
            },
        )

    def test_table_init_with_pk(self):
        t = ds.Tbl(
            name="foo",
            schemas=[{"name": "id", "dtype": "integer", "pk": True}],
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "integer"},
                        "fk": {},
                        "name": "id",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    }
                ],
                "pk": {"cols": ["id"], "of": "foo"},
                "fk": [],
            },
        )

    def test_table_model_validate(self):
        t = ds.Tbl.model_validate(
            {
                "name": "foo",
                "schemas": [
                    {"name": "id", "dtype": "integer", "pk": True},
                    {
                        "name": "name",
                        "dtype": "varchar( 256 )",
                        "nullable": False,
                    },
                ],
            },
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "integer"},
                        "fk": {},
                        "name": "id",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "varchar", "max_length": 256},
                        "fk": {},
                        "name": "name",
                        "nullable": False,
                        "pk": False,
                        "unique": False,
                    },
                ],
                "pk": {"cols": ["id"], "of": "foo"},
                "fk": [],
            },
        )
