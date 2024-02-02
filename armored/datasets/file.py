# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from typing import Literal

from ..__base import BaseUpdatableModel
from .col import Col


class BaseFl(BaseUpdatableModel):
    name: str


class CsvFl(BaseFl):
    """Csv File model"""

    type: Literal["csv"] = "csv"
    header: bool = True
    schema: list[Col]
    sep: str = ","
    comment: str = "#"
    skip_rows: int = 0
