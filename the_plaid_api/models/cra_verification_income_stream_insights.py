from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_verification_income_category import CraVerificationIncomeCategory, CraVerificationIncomeCategoryDict
from .cra_verification_income_next_payment import CraVerificationIncomeNextPayment, CraVerificationIncomeNextPaymentDict
from .cra_verification_income_provider import CraVerificationIncomeProvider, CraVerificationIncomeProviderDict
from .enums.cra_verification_income_pay_frequency import CraVerificationIncomePayFrequencyOrStr
from .enums.cra_verification_income_status import CraVerificationIncomeStatusOrStr


class CraVerificationIncomeStreamInsights(SdkBaseModel):
    """Modeled insights for a given income stream."""

    income_category: CraVerificationIncomeCategory
    """The income category for a given stream. The streams returned in the response will be filtered based on these
    primary and secondary income categories.

    See the `Income V2 Category Taxonomy <https://plaid.com/documents/income-v2-category-taxonomy.csv>`__ for a full
    list of income categories."""

    pay_frequency: CraVerificationIncomePayFrequencyOrStr
    """The income pay frequency. ``WEEKLY``: Weekly pay frequency. ``BIWEEKLY``: Biweekly pay frequency.
    ``SEMI_MONTHLY``: Semi-monthly pay frequency. ``MONTHLY``: Monthly pay frequency. ``DAILY``: Daily pay frequency.
    ``UNKNOWN``: Pay frequency is unknown."""

    income_provider: CraVerificationIncomeProvider | None
    """The object containing data about the income provider."""

    status: CraVerificationIncomeStatusOrStr
    """The status of the income source. ``ACTIVE``: The income source is active. ``INACTIVE``: The income source is
    inactive. ``UNKNOWN``: The income source status is unknown."""

    next_payment: CraVerificationIncomeNextPayment | None
    """Metadata of the income stream's next payment."""


class CraVerificationIncomeStreamInsightsDict(TypedDict):
    income_category: CraVerificationIncomeCategory | CraVerificationIncomeCategoryDict
    pay_frequency: CraVerificationIncomePayFrequencyOrStr
    income_provider: CraVerificationIncomeProvider | CraVerificationIncomeProviderDict | None
    status: CraVerificationIncomeStatusOrStr
    next_payment: CraVerificationIncomeNextPayment | CraVerificationIncomeNextPaymentDict | None
