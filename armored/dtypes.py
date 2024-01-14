from typing import (
    Annotated,
    Literal,
    Union,
)

from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator


class BaseType(BaseModel):
    """Base Type"""

    type: str = "base"


class StringType(BaseType):
    """String Type"""

    type: Literal["string", "str"] = "string"
    max_length: Annotated[int, Field(ge=-1)] = -1


class CharType(StringType):
    """Charactor Type

    Note: fixed-length strings
    """

    type: Literal["char"] = "char"


class VarcharType(StringType):
    """Variable Charactor Type

    Note: variable-length strings with limit
    """

    type: Literal["varchar"] = "varchar"


class TextType(BaseType):
    """Text Type

    Note: variable unlimited length strings
    """

    type: Literal["text"] = "text"


class IntegerType(BaseType):
    """Integer Type

    Note: Storage size, 4 bytes, -2147483648 to +2147483647
    """

    type: Literal["integer", "int"] = "integer"

    @field_validator("type", mode="after")
    def prepare_for_short_name(
        cls,
        value: Literal["integer", "int"],
    ) -> Literal["integer"]:
        return "integer" if value == "int" else value


class SmallIntType(BaseType):
    """Small Range Integer

    Note: Storage size, 2 bytes, -32768 to +32767
    """

    type: Literal["smallint"] = "smallint"


class BigIntType(BaseType):
    """Big Range Integer

    Note: Storage size, 8 bytes, -9223372036854775808 to +9223372036854775807
    """

    type: Literal["bigint"] = "bigint"


class ShortType(BaseType):
    ...


class LongType(BaseType):
    ...


class NumericType(BaseType):
    """Numeric Type"""

    type: Literal["numeric"] = "numeric"
    precision: Annotated[int, Field(ge=-1)] = -1
    scale: Annotated[int, Field(ge=-1)] = -1


class DecimalType(NumericType):
    """Decimal Type"""

    type: Literal["decimal"] = "decimal"


class FloatType(BaseType):
    ...


class RealType(BaseType):
    ...


class DoublePrecisionType(BaseType):
    ...


class TimestampType(BaseType):
    """Timestamp Type"""

    type: Literal["timestamp"] = "timestamp"
    precision: Annotated[int, Field(ge=-1, le=6)] = -1
    timezone: Annotated[
        bool,
        Field(description="Time zone flag"),
    ] = False


class TimeType(BaseType):
    ...


class DateType(BaseType):
    ...


class DateTimeType(BaseType):
    ...


DataTypes = Union[
    StringType,
    CharType,
    VarcharType,
    TextType,
    NumericType,
    DecimalType,
    TimestampType,
    IntegerType,
    BigIntType,
    SmallIntType,
    BaseType,
]