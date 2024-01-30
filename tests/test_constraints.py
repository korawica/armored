import unittest

import armored.constraints as const


class TestPrimaryKey(unittest.TestCase):
    def test_pk_init(self):
        t = const.PK(name="foo")
        self.assertEqual("foo", t.name)
        self.assertListEqual([], t.columns)

        t = const.PK(name="foo", columns=["col1"])
        self.assertEqual("foo", t.name)
        self.assertListEqual(["col1"], t.columns)

        t = const.PK(columns=["col1", "col2"])
        self.assertEqual("col1_col2_pk", t.name)
        self.assertListEqual(["col1", "col2"], t.columns)

    def test_pk_model_validate(self):
        t = const.PK.model_validate(
            {
                "name": "foo",
                "columns": ["col1"],
            }
        )
        self.assertEqual("foo", t.name)
        self.assertListEqual(["col1"], t.columns)


class TestReference(unittest.TestCase):
    def test_ref_init(self):
        t = const.Ref(table="foo", column="bar")
        self.assertEqual("foo", t.table)
        self.assertEqual("bar", t.column)


class TestForeignKey(unittest.TestCase):
    def test_fk_init(self):
        t = const.FK(
            name="foo",
            to="test",
            ref=const.Ref(table="bar", column="baz"),
        )
        self.assertEqual("foo", t.name)
        self.assertEqual("test", t.to)
        self.assertEqual("bar", t.ref.table)
        self.assertEqual("baz", t.ref.column)

    def test_fk_model_validate(self):
        t = const.FK.model_validate(
            {
                "name": "foo",
                "to": "test",
                "ref": {
                    "table": "bar",
                    "column": "baz",
                },
            }
        )
        self.assertEqual("foo", t.name)
        self.assertEqual("test", t.to)
        self.assertEqual("bar", t.ref.table)
        self.assertEqual("baz", t.ref.column)
