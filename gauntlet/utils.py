import re
from typing import (
    Optional,
    Tuple,
    Union,
)


def catch_str(
    value: str,
    key: str,
    *,
    replace: Optional = None,
    flag: bool = True,
) -> Tuple[str, Optional[Union[bool, str]]]:
    """Catch keyword from string value and return True if exits"""
    if key in value:
        return (
            " ".join(value.replace(key, (replace or "")).split()),
            (True if flag else key),
        )
    return value, (False if flag else None)


def split_dtype(dtype: str) -> Tuple[str, str]:
    """Split the datatype value from long string by null string"""
    _nullable: str = "null"
    for null_str in ["not null", "null"]:
        if re.search(null_str, dtype):
            _nullable = null_str
            dtype = dtype.replace(null_str, "")
    return " ".join(dtype.strip().split()), _nullable


def only_one(
    check_list: list,
    match_list: list,
    default: bool = True,
) -> Optional:
    """
    Examples:
        >>> list_a = ['a', 'a', 'b']
        >>> list_b = ['a', 'b', 'c']
        >>> list_c = ['d', 'f']
        >>> only_one(list_a, list_b)
        'a'
        >>> only_one(list_c, list_b)
        'a'
    """
    if len(exist := set(check_list).intersection(set(match_list))) == 1:
        return list(exist)[0]
    return next(
        (_ for _ in match_list if _ in check_list),
        (match_list[0] if default else None),
    )
