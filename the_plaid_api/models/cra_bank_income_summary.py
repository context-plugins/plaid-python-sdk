from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .cra_bank_income_historical_summary import CraBankIncomeHistoricalSummary, CraBankIncomeHistoricalSummaryDict
from .credit_amount_with_currency import CreditAmountWithCurrency, CreditAmountWithCurrencyDict


class CraBankIncomeSummary(SdkBaseModel):
    """This is a V1 (II1) schema. For the V2 (II2) equivalent, use ``CraIncomeInsightsUserSummary``. Summary for income
    across all income sources and items (max history of 730 days)."""

    total_amounts: Optional[list[CreditAmountWithCurrency]] = UNSET
    """Total amount of earnings across all the income sources in the end user's Items for the days requested by the
    client. This can contain multiple amounts, with each amount denominated in one unique currency."""

    start_date: Optional[Date] = UNSET
    """The earliest date within the days requested in which all income sources identified by Plaid appear in a user's
    account. The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[Date] = UNSET
    """The latest date in which all income sources identified by Plaid appear in the user's account. The date will be
    returned in an ISO 8601 format (YYYY-MM-DD)."""

    income_sources_count: Optional[int] = UNSET
    """Number of income sources per end user."""

    income_categories_count: Optional[int] = UNSET
    """Number of income categories per end user."""

    income_transactions_count: Optional[int] = UNSET
    """Number of income transactions per end user."""

    historical_average_monthly_gross_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """An estimate of the average gross monthly income based on the historical net amount and income category for the
    income source(s). The average monthly income is calculated based on the lifetime of the income stream, rather than
    the entire historical period included in the scope of the report."""

    historical_average_monthly_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """The average monthly income amount estimated based on the historical data for the income source(s). The average
    monthly income is calculated based on the lifetime of the income stream, rather than the entire historical period
    included in the scope of the report."""

    forecasted_average_monthly_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """The predicted average monthly income amount for the income source(s)."""

    historical_annual_gross_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """An estimate of the annual gross income for the income source, calculated by multiplying the
    ``historical_average_monthly_gross_income`` by 12."""

    historical_annual_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """An estimate of the annual net income for the income source, calculated by multiplying the
    ``historical_average_monthly_income`` by 12."""

    forecasted_annual_income: Optional[list[CreditAmountWithCurrency]] = UNSET
    """The predicted average annual income amount for the income source(s)."""

    historical_summary: Optional[list[CraBankIncomeHistoricalSummary]] = UNSET


class CraBankIncomeSummaryDict(TypedDict):
    total_amounts: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    income_sources_count: NotRequired[int]
    income_categories_count: NotRequired[int]
    income_transactions_count: NotRequired[int]
    historical_average_monthly_gross_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    historical_average_monthly_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    forecasted_average_monthly_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    historical_annual_gross_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    historical_annual_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    forecasted_annual_income: NotRequired[list[CreditAmountWithCurrency | CreditAmountWithCurrencyDict]]
    historical_summary: NotRequired[list[CraBankIncomeHistoricalSummary | CraBankIncomeHistoricalSummaryDict]]
