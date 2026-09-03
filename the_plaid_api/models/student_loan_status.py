from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .enums.type2 import Type2OrStr


class StudentLoanStatus(SdkBaseModel):
    """An object representing the status of the student loan"""

    end_date: Date | None
    """The date until which the loan will be in its current status. Dates are returned in an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    type_: Type2OrStr | None = Field(alias="type")
    """The status type of the student loan"""


class StudentLoanStatusDict(TypedDict):
    end_date: Date | None
    type_: Type2OrStr | None
