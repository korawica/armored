# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from typing import (
    Annotated,
    Optional,
)

from pydantic import BaseModel, Field
from pydantic.functional_validators import model_validator


class Const(BaseModel):
    name: Annotated[
        Optional[str],
        Field(description="Name of Constraint"),
    ] = None


class Pk(Const):
    """Primary Key Model"""

    name: Annotated[
        Optional[str],
        Field(description="Name of Primary Key Constraint"),
    ] = None
    columns: Annotated[list[str], Field(default_factory=list)]

    @model_validator(mode="after")
    def generate_name(self):
        if self.name is None and self.columns:
            self.name: str = f'{"_".join(self.columns)}_pk'
        return self


class Ref(BaseModel):
    """Reference Model"""

    table: str
    column: str


class Fk(Const):
    """Foreign Key Model
    Examples
    *   {
            "name": "foo_bar_ref_table_ref_column_fk",
            "to": "bar",
            "ref": {
                "table": "ref_table",
                "column": "ref_column"
            }
        }
    *   {
            "to": "bar",
            "ref": {
                "table": "ref_table",
                "column": "ref_column"
            }
        }
    """

    name: Annotated[
        Optional[str],
        Field(description="Name of Foreign Key Constraint"),
    ] = None
    to: str
    ref: Ref

    @model_validator(mode="after")
    def generate_name(self):
        if self.name is None:
            self.name: str = f"{self.to}_{self.ref.table}_{self.ref.column}_fk"
        return self
