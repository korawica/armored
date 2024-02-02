import unittest

import yaml
from pydantic import BaseModel

from armored.datasets.db import Tbl


class Schema(BaseModel):
    name: str
    objects: list[Tbl]


class CatalogExample(unittest.TestCase):
    def test_schema_parser(self):
        config = yaml.safe_load(
            """
        name: "warehouse"
        objects:
          - name: "customer_master"
            feature:
              - name: "id"
                dtype: "integer"
                pk: true
              - name: "name"
                dtype: "varchar( 256 )"
                nullable: false
        """
        )
        schema = Schema.model_validate(config)
        self.assertEqual(1, len(schema.objects))
