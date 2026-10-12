from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_verification_income_item import CraVerificationIncomeItem, CraVerificationIncomeItemDict
from .cra_verification_income_stream import CraVerificationIncomeStream, CraVerificationIncomeStreamDict
from .cra_verification_income_user_summary import CraVerificationIncomeUserSummary, CraVerificationIncomeUserSummaryDict


class CraVerificationIncomeReport(SdkBaseModel):
    """An object representing an Income Report within the Home Lending Report."""

    generated_time: RFC3339DateTime
    """The time when the Home Lending Income Report was generated."""

    days_requested: int
    """The number of days requested by the customer for the Home Lending Income Report."""

    user_summary: CraVerificationIncomeUserSummary | None
    """Aggregated summary of all income streams for this user."""

    income_streams: list[CraVerificationIncomeStream]
    """The list of income streams for this user."""

    items: list[CraVerificationIncomeItem]
    """The list of Items in the report along with the associated metadata about the Item."""


class CraVerificationIncomeReportDict(TypedDict):
    generated_time: RFC3339DateTime
    days_requested: int
    user_summary: CraVerificationIncomeUserSummaryDict | None
    income_streams: list[CraVerificationIncomeStreamDict]
    items: list[CraVerificationIncomeItemDict]
