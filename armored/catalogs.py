import re
from typing import (
    Annotated,
    Any,
    Optional,
    Union,
)

from pydantic import (
    Field,
    field_validator,
    model_validator,
)

from .base import BaseUpdatableModel
from .constraints import Reference
from .dtypes import DataTypes
from .settings import ColumnSetting
from .utils import (
    catch_str,
    extract_dtype,
    only_one,
    split_dtype,
)


class BaseColumn(BaseUpdatableModel):
    """Base Column Model"""

    name: Annotated[
        str,
        Field(
            description="Name of Column",
            alias="ColumnName",
        ),
    ]
    dtype: Annotated[
        DataTypes,
        Field(
            union_mode="left_to_right",
            description="Data Type of Column",
            alias="DataType",
        ),
    ]

    @field_validator("name")
    def prepare_name(cls, value: str) -> str:
        """Prepare string value of name"""
        return "".join(value.strip().split())

    @field_validator("dtype", mode="before")
    def prepare_str2dtype(cls, value: Union[str, dict, DataTypes]):
        """Prepare string value of dtype"""
        if isinstance(value, str):
            return extract_dtype(value)
        return value


class Column(BaseColumn):
    """Column model"""

    nullable: Annotated[
        bool,
        Field(
            description="Nullable flag",
            alias="Nullable",
        ),
    ] = True
    unique: Annotated[
        bool,
        Field(
            description="Unique flag",
            alias="Unique",
        ),
    ] = False
    default: Annotated[
        Union[int, str, None],
        Field(
            description="Default value for this column",
            alias="Default",
        ),
    ] = None
    check: Annotated[
        Optional[str],
        Field(
            description="Check Statement",
            alias="Check",
        ),
    ] = None

    # Special value that effect to parent model that include this model
    pk: Annotated[
        bool,
        Field(
            description="Primary key flag which can not contain null value",
            alias="PrimaryKey",
        ),
    ] = False
    fk: Annotated[
        Union[Reference, dict],
        Field(
            default_factory=dict,
            description="Foreign key reference",
            alias="ForeignKey",
        ),
    ]

    @classmethod
    def extract_column_from_dtype(cls, value: str) -> dict[str, Any]:
        values: dict[str, Any] = {"nullable": False}
        _dtype, _nullable = split_dtype(value)

        # Remove unique value from datatype
        _dtype, values["unique"] = catch_str(_dtype, key="unique")

        # Remove primary key value from datatype
        _dtype, values["pk"] = catch_str(_dtype, key="primary key")

        # Rename serial value to int from datatype
        _dtype, serial_flag = catch_str(_dtype, key="serial", replace="integer")

        if "check" in _dtype:
            if m := re.search(
                r"check\s?\((?P<check>[^()]*(?:\(.*\))*[^()]*)\)",
                _dtype,
            ):
                _dtype, values["check"] = catch_str(
                    _dtype, m.group(), flag=False
                )
            else:
                raise ValueError(
                    "datatype with type string does not support for "
                    "this format of check"
                )

        if re.search("default", _dtype):
            _dtype, _default = _dtype.split("default", maxsplit=1)
            values["dtype"] = _dtype.strip()
            values["default"] = _default.strip()
        else:
            values["dtype"] = _dtype

            if serial_flag:
                _nullable: str = "not null"
                values["default"] = "nextval('tablename_colname_seq')"

        values["nullable"] = not re.search("not null", _nullable)
        return values

    @model_validator(mode="before")
    def prepare_dtype(cls, values):
        """Prepare datatype value that parsing to this model with different
        types, string or dict type.

        This filter will prepare datatype value from the format,
            {DATATYPE} {UNIQUE} {NULLABLE} {DEFAULT}
            {PRIMARY KEY|FOREIGN KEY} {CHECK}

        Examples:
        - varchar( 100 ) not null default 'O' check( <name> <> 'test' )
        - serial not null primary key
        """
        if not (
            dtype_key := only_one(values, ColumnSetting.dtype, default=False)
        ):
            raise ValueError("dtype key does not contain in values")

        pre_dtype: Any = values.pop(dtype_key)
        values_update: dict[str, Any] = {}
        if isinstance(pre_dtype, str):
            values_update = cls.extract_column_from_dtype(pre_dtype)
        else:
            values["dtype"] = pre_dtype

        return values_update | values

    @model_validator(mode="after")
    def validate_logic(self):
        """Validate and check logic of values"""
        pk: bool = self.pk
        nullable: bool = self.nullable

        # primary key and nullable does not True together
        if pk and nullable:
            raise ValueError("`pk` and `nullable` can not be True together")
        return self
