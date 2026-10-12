from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .total_report_inflow_amount import TotalReportInflowAmount, TotalReportInflowAmountDict
from .total_report_inflow_amount30_d import TotalReportInflowAmount30D, TotalReportInflowAmount30DDict
from .total_report_inflow_amount60_d import TotalReportInflowAmount60D, TotalReportInflowAmount60DDict
from .total_report_inflow_amount90_d import TotalReportInflowAmount90D, TotalReportInflowAmount90DDict
from .total_report_outflow_amount import TotalReportOutflowAmount, TotalReportOutflowAmountDict
from .total_report_outflow_amount30_d import TotalReportOutflowAmount30D, TotalReportOutflowAmount30DDict
from .total_report_outflow_amount60_d import TotalReportOutflowAmount60D, TotalReportOutflowAmount60DDict
from .total_report_outflow_amount90_d import TotalReportOutflowAmount90D, TotalReportOutflowAmount90DDict


class BaseReportUserAttributes(SdkBaseModel):
    """Calculated attributes derived from transaction-level data, aggregated across accounts."""

    nsf_overdraft_transactions_count: Optional[int] = UNSET
    """The number of net NSF fee transactions in the time range for the report (not counting any fees that were reversed
    within that time range)."""

    nsf_overdraft_transactions_count_30d: Optional[int] = UNSET
    """The number of net NSF fee transactions in the last 30 days in the report (not counting any fees that were
    reversed within that time range)."""

    nsf_overdraft_transactions_count_60d: Optional[int] = UNSET
    """The number of net NSF fee transactions in the last 60 days in the report (not counting any fees that were
    reversed within that time range)."""

    nsf_overdraft_transactions_count_90d: Optional[int] = UNSET
    """The number of net NSF fee transactions in the last 90 days in the report (not counting any fees that were
    reversed within that time range)."""

    total_inflow_amount: OptionalNullable[TotalReportInflowAmount] = UNSET
    """Total amount of debit transactions into the report's accounts in the time period of the report. This field only
    takes into account USD transactions from the accounts."""

    total_inflow_amount_30d: OptionalNullable[TotalReportInflowAmount30D] = UNSET
    """Total amount of debit transactions into the report's accounts in the last 30 days. This field only takes into
    account USD transactions from the accounts."""

    total_inflow_amount_60d: OptionalNullable[TotalReportInflowAmount60D] = UNSET
    """Total amount of debit transactions into the report's accounts in the last 60 days. This field only takes into
    account USD transactions from the accounts."""

    total_inflow_amount_90d: OptionalNullable[TotalReportInflowAmount90D] = UNSET
    """Total amount of debit transactions into the report's accounts in the last 90 days. This field only takes into
    account USD transactions from the accounts."""

    total_outflow_amount: OptionalNullable[TotalReportOutflowAmount] = UNSET
    """Total amount of credit transactions out of the report's accounts in the time period of the report. This field
    only takes into account USD transactions from the accounts."""

    total_outflow_amount_30d: OptionalNullable[TotalReportOutflowAmount30D] = UNSET
    """Total amount of credit transactions out of the report's accounts in the last 30 days. This field only takes into
    account USD transactions from the accounts."""

    total_outflow_amount_60d: OptionalNullable[TotalReportOutflowAmount60D] = UNSET
    """Total amount of credit transactions out of the report's accounts in the last 60 days. This field only takes into
    account USD transactions from the accounts."""

    total_outflow_amount_90d: OptionalNullable[TotalReportOutflowAmount90D] = UNSET
    """Total amount of credit transactions out of the report's accounts in the last 90 days. This field only takes into
    account USD transactions from the accounts."""


class BaseReportUserAttributesDict(TypedDict):
    nsf_overdraft_transactions_count: NotRequired[int]
    nsf_overdraft_transactions_count_30d: NotRequired[int]
    nsf_overdraft_transactions_count_60d: NotRequired[int]
    nsf_overdraft_transactions_count_90d: NotRequired[int]
    total_inflow_amount: NotRequired[TotalReportInflowAmountDict | None]
    total_inflow_amount_30d: NotRequired[TotalReportInflowAmount30DDict | None]
    total_inflow_amount_60d: NotRequired[TotalReportInflowAmount60DDict | None]
    total_inflow_amount_90d: NotRequired[TotalReportInflowAmount90DDict | None]
    total_outflow_amount: NotRequired[TotalReportOutflowAmountDict | None]
    total_outflow_amount_30d: NotRequired[TotalReportOutflowAmount30DDict | None]
    total_outflow_amount_60d: NotRequired[TotalReportOutflowAmount60DDict | None]
    total_outflow_amount_90d: NotRequired[TotalReportOutflowAmount90DDict | None]
