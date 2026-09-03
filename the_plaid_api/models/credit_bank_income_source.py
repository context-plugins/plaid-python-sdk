from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .credit_bank_income_historical_summary import (
    CreditBankIncomeHistoricalSummary,
    CreditBankIncomeHistoricalSummaryDict,
)
from .enums.credit_bank_income_category import CreditBankIncomeCategoryOrStr
from .enums.credit_bank_income_pay_frequency import CreditBankIncomePayFrequencyOrStr


class CreditBankIncomeSource(SdkBaseModel):
    """Detailed information for the income source."""

    income_source_id: Optional[str] = UNSET
    """A unique identifier for an income source."""

    income_description: Optional[str] = UNSET
    """The most common name or original description for the underlying income transactions."""

    income_category: Optional[CreditBankIncomeCategoryOrStr] = UNSET
    """The income category. ``BANK_INTEREST``: Interest earned from a bank account. ``BENEFIT_OTHER``: Government
    benefits other than retirement, unemployment, child support, or disability. Currently used only in the UK, to
    represent benefits such as Cost of Living Payments. ``CASH``: Deprecated and used only for existing legacy
    implementations. Has been replaced by ``CASH_DEPOSIT`` and ``TRANSFER_FROM_APPLICATION``. ``CASH_DEPOSIT``: A cash
    or check deposit. ``CHILD_SUPPORT``: Child support payments received. ``GIG_ECONOMY``: Income earned as a gig
    economy worker, e.g. driving for Uber, Lyft, Postmates, DoorDash, etc. ``LONG_TERM_DISABILITY``: Disability
    payments, including Social Security disability benefits. ``OTHER``: Income that could not be categorized as any
    other income category. ``MILITARY``: Veterans benefits. Income earned as salary for serving in the military (e.g.
    through DFAS) will be classified as ``SALARY`` rather than ``MILITARY``. ``RENTAL``: Income earned from a rental
    property. Income may be identified as rental when the payment is received through a rental platform, e.g. Airbnb;
    rent paid directly by the tenant to the property owner (e.g. via cash, check, or ACH) will typically not be
    classified as rental income. ``RETIREMENT``: Payments from private retirement systems, pensions, and government
    retirement programs, including Social Security retirement benefits. ``SALARY``: Payment from an employer to an
    earner or other form of permanent employment. ``TAX_REFUND``: A tax refund. ``TRANSFER_FROM_APPLICATION``: Deposits
    from a money transfer app, such as Venmo, Cash App, or Zelle. ``UNEMPLOYMENT``: Unemployment benefits. In the UK,
    includes certain low-income benefits such as the Universal Credit."""

    account_id: Optional[str] = UNSET
    """Plaid's unique identifier for the account."""

    start_date: Optional[Date] = UNSET
    """Minimum of all dates within the specific income sources in the user's bank account for days requested by the
    client. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[Date] = UNSET
    """Maximum of all dates within the specific income sources in the user's bank account for days requested by the
    client. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    pay_frequency: Optional[CreditBankIncomePayFrequencyOrStr] = UNSET
    """The income pay frequency."""

    total_amount: Optional[float] = UNSET
    """Total amount of earnings in the user's bank account for the specific income source for days requested by the
    client."""

    transaction_count: Optional[int] = UNSET
    """Number of transactions for the income source within the start and end date."""

    historical_summary: Optional[list[CreditBankIncomeHistoricalSummary]] = UNSET


class CreditBankIncomeSourceDict(TypedDict):
    income_source_id: NotRequired[str]
    income_description: NotRequired[str]
    income_category: NotRequired[CreditBankIncomeCategoryOrStr]
    account_id: NotRequired[str]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    pay_frequency: NotRequired[CreditBankIncomePayFrequencyOrStr]
    total_amount: NotRequired[float]
    transaction_count: NotRequired[int]
    historical_summary: NotRequired[list[CreditBankIncomeHistoricalSummary | CreditBankIncomeHistoricalSummaryDict]]
