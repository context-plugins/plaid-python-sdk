from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.income_verification_precheck_confidence import IncomeVerificationPrecheckConfidenceOrStr


class CreditPayrollIncomePrecheckResponse(SdkBaseModel):
    """Defines the response schema for ``/credit/payroll_income/precheck``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    confidence: IncomeVerificationPrecheckConfidenceOrStr
    """The confidence that Plaid can support the user in the digital income verification flow instead of requiring a
    manual paystub upload. One of the following:

    ``"HIGH"``: It is very likely that this user can use the digital income verification flow.

    "``LOW``": It is unlikely that this user can use the digital income verification flow.

    ``"UNKNOWN"``: It was not possible to determine if the user is supportable with the information passed."""


class CreditPayrollIncomePrecheckResponseDict(TypedDict):
    request_id: str
    confidence: IncomeVerificationPrecheckConfidenceOrStr
