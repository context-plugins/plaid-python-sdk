from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .total_inflow_amount import TotalInflowAmount, TotalInflowAmountDict
from .total_inflow_amount30_d import TotalInflowAmount30D, TotalInflowAmount30DDict
from .total_inflow_amount60_d import TotalInflowAmount60D, TotalInflowAmount60DDict
from .total_inflow_amount90_d import TotalInflowAmount90D, TotalInflowAmount90DDict
from .total_outflow_amount import TotalOutflowAmount, TotalOutflowAmountDict
from .total_outflow_amount30_d import TotalOutflowAmount30D, TotalOutflowAmount30DDict
from .total_outflow_amount60_d import TotalOutflowAmount60D, TotalOutflowAmount60DDict
from .total_outflow_amount90_d import TotalOutflowAmount90D, TotalOutflowAmount90DDict


class BaseReportAttributes(SdkBaseModel):
    """Calculated attributes derived from transaction-level data."""

    is_primary_account: OptionalNullable[bool] = UNSET
    """Prediction indicator of whether the account is a primary account. Only one account per account type across the
    items connected will have a value of true."""

    primary_account_score: OptionalNullable[float] = UNSET
    """Value ranging from 0-1. The higher the score, the more confident we are of the account being the primary
    account."""

    nsf_overdraft_transactions_count: Optional[int] = UNSET
    """The number of net NSF fee transactions for a given account within the report time range (not counting any fees
    that were reversed within the time range)."""

    nsf_overdraft_transactions_count_30d: Optional[int] = UNSET
    """The number of net NSF fee transactions within the last 30 days for a given account (not counting any fees that
    were reversed within the time range)."""

    nsf_overdraft_transactions_count_60d: Optional[int] = UNSET
    """The number of net NSF fee transactions within the last 60 days for a given account (not counting any fees that
    were reversed within the time range)."""

    nsf_overdraft_transactions_count_90d: Optional[int] = UNSET
    """The number of net NSF fee transactions within the last 90 days for a given account (not counting any fees that
    were reversed within the time range)."""

    total_inflow_amount: OptionalNullable[TotalInflowAmount] = UNSET
    """Total amount of debit transactions into the account in the time period of the report. This field will be empty
    for non-depository accounts. This field only takes into account USD transactions from the account."""

    total_inflow_amount_30d: OptionalNullable[TotalInflowAmount30D] = UNSET
    """Total amount of debit transactions into the account in the last 30 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    total_inflow_amount_60d: OptionalNullable[TotalInflowAmount60D] = UNSET
    """Total amount of debit transactions into the account in the last 60 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    total_inflow_amount_90d: OptionalNullable[TotalInflowAmount90D] = UNSET
    """Total amount of debit transactions into the account in the last 90 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    total_outflow_amount: OptionalNullable[TotalOutflowAmount] = UNSET
    """Total amount of credit transactions out of the account in the time period of the report. This field will be empty
    for non-depository accounts. This field only takes into account USD transactions from the account."""

    total_outflow_amount_30d: OptionalNullable[TotalOutflowAmount30D] = UNSET
    """Total amount of credit transactions out of the account in the last 30 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    total_outflow_amount_60d: OptionalNullable[TotalOutflowAmount60D] = UNSET
    """Total amount of credit transactions out of the account in the last 60 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""

    total_outflow_amount_90d: OptionalNullable[TotalOutflowAmount90D] = UNSET
    """Total amount of credit transactions out of the account in the last 90 days. This field will be empty for
    non-depository accounts. This field only takes into account USD transactions from the account."""


class BaseReportAttributesDict(TypedDict):
    is_primary_account: NotRequired[bool | None]
    primary_account_score: NotRequired[float | None]
    nsf_overdraft_transactions_count: NotRequired[int]
    nsf_overdraft_transactions_count_30d: NotRequired[int]
    nsf_overdraft_transactions_count_60d: NotRequired[int]
    nsf_overdraft_transactions_count_90d: NotRequired[int]
    total_inflow_amount: NotRequired[TotalInflowAmount | TotalInflowAmountDict | None]
    total_inflow_amount_30d: NotRequired[TotalInflowAmount30D | TotalInflowAmount30DDict | None]
    total_inflow_amount_60d: NotRequired[TotalInflowAmount60D | TotalInflowAmount60DDict | None]
    total_inflow_amount_90d: NotRequired[TotalInflowAmount90D | TotalInflowAmount90DDict | None]
    total_outflow_amount: NotRequired[TotalOutflowAmount | TotalOutflowAmountDict | None]
    total_outflow_amount_30d: NotRequired[TotalOutflowAmount30D | TotalOutflowAmount30DDict | None]
    total_outflow_amount_60d: NotRequired[TotalOutflowAmount60D | TotalOutflowAmount60DDict | None]
    total_outflow_amount_90d: NotRequired[TotalOutflowAmount90D | TotalOutflowAmount90DDict | None]
