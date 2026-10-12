from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .cra_bank_income_item import CraBankIncomeItem, CraBankIncomeItemDict
from .cra_bank_income_summary import CraBankIncomeSummary, CraBankIncomeSummaryDict
from .cra_bank_income_warning import CraBankIncomeWarning, CraBankIncomeWarningDict
from .cra_income_insights_user_summary import CraIncomeInsightsUserSummary, CraIncomeInsightsUserSummaryDict
from .cra_income_stream import CraIncomeStream, CraIncomeStreamDict


class CraIncomeInsights(SdkBaseModel):
    """The Check Income Insights Report for an end user."""

    report_id: Optional[str] = UNSET
    """The unique identifier associated with the Check Income Insights Report."""

    generated_time: Optional[RFC3339DateTime] = UNSET
    """The time when the Check Income Insights Report was generated."""

    days_requested: Optional[int] = UNSET
    """The number of days requested by the customer for the Check Income Insights Report."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    items: Optional[list[CraBankIncomeItem]] = UNSET
    """The list of Items in the report along with the associated metadata about the Item."""

    user_summary: OptionalNullable[CraIncomeInsightsUserSummary] = UNSET
    """Aggregated summary of all income streams for this user."""

    income_streams: list[CraIncomeStream]
    """The list of income streams for this user."""

    bank_income_summary: Optional[CraBankIncomeSummary] = UNSET
    """This is a V1 (II1) schema. For the V2 (II2) equivalent, use ``CraIncomeInsightsUserSummary``. Summary for income
    across all income sources and items (max history of 730 days)."""

    warnings: Optional[list[CraBankIncomeWarning]] = UNSET
    """If data from the report was unable to be retrieved, the warnings object will contain information about the error
    that caused the data to be incomplete."""


class CraIncomeInsightsDict(TypedDict):
    report_id: NotRequired[str]
    generated_time: NotRequired[RFC3339DateTime]
    days_requested: NotRequired[int]
    client_report_id: NotRequired[str | None]
    items: NotRequired[list[CraBankIncomeItemDict]]
    user_summary: NotRequired[CraIncomeInsightsUserSummaryDict | None]
    income_streams: list[CraIncomeStreamDict]
    bank_income_summary: NotRequired[CraBankIncomeSummaryDict]
    warnings: NotRequired[list[CraBankIncomeWarningDict]]
