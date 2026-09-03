from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_bank_income_income_provider import CraBankIncomeIncomeProvider, CraBankIncomeIncomeProviderDict
from .cra_income_category import CraIncomeCategory, CraIncomeCategoryDict
from .cra_income_next_payment import CraIncomeNextPayment, CraIncomeNextPaymentDict
from .enums.cra_bank_income_status import CraBankIncomeStatusOrStr
from .enums.credit_bank_income_pay_frequency import CreditBankIncomePayFrequencyOrStr


class CraIncomeStreamInsights(SdkBaseModel):
    """Modeled insights for a given income stream."""

    income_category: CraIncomeCategory
    """The income category for a given stream. The streams returned in the response will be filtered based on these
    primary and secondary income categories.

    See the `Income V2 Category Taxonomy <https://plaid.com/documents/income-v2-category-taxonomy.csv>`__ for a full
    list of income categories."""

    pay_frequency: CreditBankIncomePayFrequencyOrStr
    """The income pay frequency."""

    income_provider: CraBankIncomeIncomeProvider | None
    """The object containing data about the income provider."""

    status: CraBankIncomeStatusOrStr
    """The status of the income sources. ``ACTIVE``: The income source is active. ``INACTIVE``: The income source is
    inactive. ``UNKNOWN``: The income source status is unknown."""

    next_payment: CraIncomeNextPayment | None
    """Metadata of the income stream's next payment."""


class CraIncomeStreamInsightsDict(TypedDict):
    income_category: CraIncomeCategory | CraIncomeCategoryDict
    pay_frequency: CreditBankIncomePayFrequencyOrStr
    income_provider: CraBankIncomeIncomeProvider | CraBankIncomeIncomeProviderDict | None
    status: CraBankIncomeStatusOrStr
    next_payment: CraIncomeNextPayment | CraIncomeNextPaymentDict | None
