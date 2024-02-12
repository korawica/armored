# Utility Package: *Armored*

[![test](https://github.com/korawica/armored/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/armored/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/korawica/armored/graph/badge.svg?token=OOUHC5SW4A)](https://codecov.io/gh/korawica/armored)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/armored?logo=pypi)](https://pypi.org/project/armored/)
[![size](https://img.shields.io/github/languages/code-size/korawica/armored)](https://github.com/korawica/armored)

**Table of Contents**:

- [Installation](#installation)
- [Models](#models)
  - [Data Types](#data-types)
  - [Constraints](#constraints)
  - [Datasets](#datasets)
  - [Lineages](#lineages)
- [Enums](#enums)
- [Usecase](#usecase)

This models package, **Armored**, implements any model objects for **Data Pipeline**
or **Data Platform**. The Model objects was implemented from the [Pydantic V2](https://docs.pydantic.dev/latest/).

The model able to handle common logic validations and able to adjust by custom code
for your specific requirements (Yeah, it just inherits Sub-Class from `BaseModel`).

## Installation

```shell
pip install -U armored
```

## Models

### Data Types

```python
from armored.dtype import StringType

dtype = StringType()
assert dtype.type == "string"
assert dtype.max_length == -1
```

### Constraints

```python
from armored.const import Pk

const = Pk(of="foo", cols=["bar", "baz"])
assert const.name == "foo_bar_baz_pk"
assert const.cols == ["bar", "baz"]
```

### Datasets

```python
from armored.datasets import Col, Tbl

col = Col(name="foo", dtype="varchar( 100 )")
assert "foo" == col.name
assert "varchar" == col.dtype.type
assert 100 == col.dtype.max_length

tbl = Tbl(
    name="foo",
    feature=[
        Col(name="id", dtype="integer primary key"),
        Col(name="foo", dtype="varchar( 10 )"),
    ],
)
assert "foo" == tbl.name
assert "id" == tbl.feature[0].name
```

### Lineages

## Enums

## Usecase

If I have some catalog config, it easy to pass this config to model object.

```python
import yaml
from pydantic import BaseModel
from armored.datasets import Tbl


class Schema(BaseModel):
    name: str
    objects: list[Tbl]


config = yaml.safe_load("""
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
""")
feature = Schema.model_validate(config)
assert 1 == len(feature.objects)
```

## License

This project was licensed under the terms of the [MIT license](LICENSE).
