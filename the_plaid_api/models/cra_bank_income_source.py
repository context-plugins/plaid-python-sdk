from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .cra_bank_income_employer import CraBankIncomeEmployer, CraBankIncomeEmployerDict
from .cra_bank_income_historical_summary import CraBankIncomeHistoricalSummary, CraBankIncomeHistoricalSummaryDict
from .cra_bank_income_income_provider import CraBankIncomeIncomeProvider, CraBankIncomeIncomeProviderDict
from .cra_prediction_interval import CraPredictionInterval, CraPredictionIntervalDict
from .enums.cra_bank_income_status import CraBankIncomeStatusOrStr
from .enums.credit_bank_income_category import CreditBankIncomeCategoryOrStr
from .enums.credit_bank_income_pay_frequency import CreditBankIncomePayFrequencyOrStr


class CraBankIncomeSource(SdkBaseModel):
    """Detailed information for the income source."""

    account_id: Optional[str] = UNSET
    """The account ID with which this income source is associated."""

    income_source_id: Optional[str] = UNSET
    """A unique identifier for an income source. If the report is regenerated and a new ``report_id`` is created, the
    new report will have a new set of ``income_source_id``s."""

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

    iso_currency_code: OptionalNullable[str] = UNSET
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: OptionalNullable[str] = UNSET
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""

    transaction_count: Optional[int] = UNSET
    """Number of transactions for the income source within the start and end date."""

    next_payment_date: OptionalNullable[Date] = UNSET
    """The expected date of the end user's next paycheck for the income source. The date will be returned in an ISO 8601
    format (YYYY-MM-DD)."""

    status: Optional[CraBankIncomeStatusOrStr] = UNSET
    """The status of the income sources. ``ACTIVE``: The income source is active. ``INACTIVE``: The income source is
    inactive. ``UNKNOWN``: The income source status is unknown."""

    historical_average_monthly_gross_income: OptionalNullable[float] = UNSET
    """An estimate of the average gross monthly income based on the historical net amount and income category for the
    income source(s)."""

    historical_average_monthly_income: OptionalNullable[float] = UNSET
    """The average monthly net income amount estimated based on the historical data for the income source(s)."""

    forecasted_average_monthly_income: OptionalNullable[float] = UNSET
    """The predicted average monthly net income amount for the income source(s)."""

    forecasted_average_monthly_income_prediction_intervals: list[CraPredictionInterval]
    """The prediction interval(s) for the forecasted average monthly income."""

    employer: Optional[CraBankIncomeEmployer] = UNSET
    """The object containing employer data."""

    income_provider: CraBankIncomeIncomeProvider | None
    """The object containing data about the income provider."""

    historical_summary: Optional[list[CraBankIncomeHistoricalSummary]] = UNSET


class CraBankIncomeSourceDict(TypedDict):
    account_id: NotRequired[str]
    income_source_id: NotRequired[str]
    income_description: NotRequired[str]
    income_category: NotRequired[CreditBankIncomeCategoryOrStr]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    pay_frequency: NotRequired[CreditBankIncomePayFrequencyOrStr]
    total_amount: NotRequired[float]
    iso_currency_code: NotRequired[str | None]
    unofficial_currency_code: NotRequired[str | None]
    transaction_count: NotRequired[int]
    next_payment_date: NotRequired[Date | None]
    status: NotRequired[CraBankIncomeStatusOrStr]
    historical_average_monthly_gross_income: NotRequired[float | None]
    historical_average_monthly_income: NotRequired[float | None]
    forecasted_average_monthly_income: NotRequired[float | None]
    forecasted_average_monthly_income_prediction_intervals: list[CraPredictionIntervalDict]
    employer: NotRequired[CraBankIncomeEmployerDict]
    income_provider: CraBankIncomeIncomeProviderDict | None
    historical_summary: NotRequired[list[CraBankIncomeHistoricalSummaryDict]]
