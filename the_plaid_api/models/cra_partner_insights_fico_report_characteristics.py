from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CraPartnerInsightsFicoReportCharacteristics(SdkBaseModel):
    """Report characteristics returned by FICO describing the banking data used to generate the UltraFICO® score."""

    num_accounts: OptionalNullable[int] = UNSET
    """Total number of accounts included in the report. Limited to checking, savings, and money market accounts."""

    avg_daily_balance_over_1_month: OptionalNullable[float] = UNSET
    """Average daily balance over the past 1 month."""

    avg_daily_balance_over_3_months: OptionalNullable[float] = UNSET
    """Average daily balance over the past 3 months."""

    avg_daily_balance_over_6_months: OptionalNullable[float] = UNSET
    """Average daily balance over the past 6 months."""

    avg_daily_balance_over_12_months: OptionalNullable[float] = UNSET
    """Average daily balance over the past 12 months."""

    days_since_earliest_tx: OptionalNullable[int] = UNSET
    """Number of days since the earliest transaction in the report."""

    days_since_most_recent_negative_ending_balance: OptionalNullable[int] = UNSET
    """Number of days since the most recent day with a negative ending balance."""

    days_since_most_recent_insufficient_funds_fee_debit_tx: OptionalNullable[int] = UNSET
    """Number of days since the most recent insufficient funds fee debit transaction."""

    tot_number_days_with_negative_balance_over_1_month: OptionalNullable[int] = UNSET
    """Total number of days with a negative balance over the past 1 month."""

    tot_number_days_with_negative_balance_over_3_months: OptionalNullable[int] = UNSET
    """Total number of days with a negative balance over the past 3 months."""

    tot_number_days_with_negative_balance_over_6_months: OptionalNullable[int] = UNSET
    """Total number of days with a negative balance over the past 6 months."""

    tot_number_days_with_negative_balance_over_12_months: OptionalNullable[int] = UNSET
    """Total number of days with a negative balance over the past 12 months."""

    days_since_most_recent_tx: OptionalNullable[int] = UNSET
    """Number of days since the most recent transaction."""

    days_with_tx_over_1_month: OptionalNullable[int] = UNSET
    """Number of days with at least one transaction over the past 1 month."""

    days_with_tx_over_3_months: OptionalNullable[int] = UNSET
    """Number of days with at least one transaction over the past 3 months."""

    days_with_tx_over_6_months: OptionalNullable[int] = UNSET
    """Number of days with at least one transaction over the past 6 months."""

    days_with_tx_over_12_months: OptionalNullable[int] = UNSET
    """Number of days with at least one transaction over the past 12 months."""

    tot_current_balances: OptionalNullable[float] = UNSET
    """Sum of current balances across all accounts in the report."""

    num_checking_accounts: OptionalNullable[int] = UNSET
    """Number of checking accounts included in the report."""

    num_money_market_accounts: OptionalNullable[int] = UNSET
    """Number of money market accounts included in the report."""

    num_savings_accounts: OptionalNullable[int] = UNSET
    """Number of savings accounts included in the report."""


class CraPartnerInsightsFicoReportCharacteristicsDict(TypedDict):
    num_accounts: NotRequired[int | None]
    avg_daily_balance_over_1_month: NotRequired[float | None]
    avg_daily_balance_over_3_months: NotRequired[float | None]
    avg_daily_balance_over_6_months: NotRequired[float | None]
    avg_daily_balance_over_12_months: NotRequired[float | None]
    days_since_earliest_tx: NotRequired[int | None]
    days_since_most_recent_negative_ending_balance: NotRequired[int | None]
    days_since_most_recent_insufficient_funds_fee_debit_tx: NotRequired[int | None]
    tot_number_days_with_negative_balance_over_1_month: NotRequired[int | None]
    tot_number_days_with_negative_balance_over_3_months: NotRequired[int | None]
    tot_number_days_with_negative_balance_over_6_months: NotRequired[int | None]
    tot_number_days_with_negative_balance_over_12_months: NotRequired[int | None]
    days_since_most_recent_tx: NotRequired[int | None]
    days_with_tx_over_1_month: NotRequired[int | None]
    days_with_tx_over_3_months: NotRequired[int | None]
    days_with_tx_over_6_months: NotRequired[int | None]
    days_with_tx_over_12_months: NotRequired[int | None]
    tot_current_balances: NotRequired[float | None]
    num_checking_accounts: NotRequired[int | None]
    num_money_market_accounts: NotRequired[int | None]
    num_savings_accounts: NotRequired[int | None]
