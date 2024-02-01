# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from typing import Any, Literal

from pydantic import (
    BaseModel,
)


class BaseActivity(BaseModel):
    type: str


class CopyActivity(BaseActivity):
    type: Literal["copy"] = "copy"
    src: str
    sink: str
    options: dict[str, Any]
