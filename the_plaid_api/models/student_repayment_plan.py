from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type3 import Type3OrStr


class StudentRepaymentPlan(SdkBaseModel):
    """An object representing the repayment plan for the student loan"""

    description: str | None
    """The description of the repayment plan as provided by the servicer."""

    type_: Type3OrStr | None = Field(alias="type")
    """The type of the repayment plan."""


class StudentRepaymentPlanDict(TypedDict):
    description: str | None
    type_: Type3OrStr | None
