from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .base_report_average_flow_insights import BaseReportAverageFlowInsights, BaseReportAverageFlowInsightsDict
from .base_report_longest_gap_insights import BaseReportLongestGapInsights, BaseReportLongestGapInsightsDict
from .base_report_number_flow_insights import BaseReportNumberFlowInsights, BaseReportNumberFlowInsightsDict


class BaseReportAccountInsights(SdkBaseModel):
    """Calculated insights derived from transaction-level data. This field has been deprecated in favor of `Base Report
    attributes aggregated across accounts
    <https://plaid.com/docs/api/products/check/#cra-check_report-base_report-get-response-report-attributes>`__ and will
    be removed in a future release."""

    oldest_transaction_date: OptionalNullable[Date] = UNSET
    """Date of the earliest transaction for the account."""

    most_recent_transaction_date: OptionalNullable[Date] = UNSET
    """Date of the most recent transaction for the account."""

    days_available: Optional[int] = UNSET
    """Number of days available for the account."""

    average_days_between_transactions: Optional[float] = UNSET
    """Average number of days between sequential transactions"""

    longest_gaps_between_transactions: Optional[list[BaseReportLongestGapInsights]] = UNSET
    """Longest gap between sequential transactions in a time period. This array can include multiple time periods."""

    number_of_inflows: Optional[list[BaseReportNumberFlowInsights]] = UNSET
    """The number of debits into the account. This array will be empty for non-depository accounts."""

    average_inflow_amounts: Optional[list[BaseReportAverageFlowInsights]] = UNSET
    """Average amount of debit transactions into the account in a time period. This array will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    number_of_outflows: Optional[list[BaseReportNumberFlowInsights]] = UNSET
    """The number of outflows from the account. This array will be empty for non-depository accounts."""

    average_outflow_amounts: Optional[list[BaseReportAverageFlowInsights]] = UNSET
    """Average amount of transactions out of the account in a time period. This array will be empty for non-depository
    accounts. This field only takes into account USD transactions from the account."""

    number_of_days_no_transactions: Optional[int] = UNSET
    """Number of days with no transactions"""


class BaseReportAccountInsightsDict(TypedDict):
    oldest_transaction_date: NotRequired[Date | None]
    most_recent_transaction_date: NotRequired[Date | None]
    days_available: NotRequired[int]
    average_days_between_transactions: NotRequired[float]
    longest_gaps_between_transactions: NotRequired[
        list[BaseReportLongestGapInsights | BaseReportLongestGapInsightsDict]
    ]
    number_of_inflows: NotRequired[list[BaseReportNumberFlowInsights | BaseReportNumberFlowInsightsDict]]
    average_inflow_amounts: NotRequired[list[BaseReportAverageFlowInsights | BaseReportAverageFlowInsightsDict]]
    number_of_outflows: NotRequired[list[BaseReportNumberFlowInsights | BaseReportNumberFlowInsightsDict]]
    average_outflow_amounts: NotRequired[list[BaseReportAverageFlowInsights | BaseReportAverageFlowInsightsDict]]
    number_of_days_no_transactions: NotRequired[int]
