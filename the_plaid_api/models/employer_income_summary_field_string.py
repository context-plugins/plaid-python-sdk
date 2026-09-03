from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.verification_status import VerificationStatusOrStr


class EmployerIncomeSummaryFieldString(SdkBaseModel):
    """The name of the employer, as reported on the paystub."""

    value: str
    """The value of the field."""

    verification_status: VerificationStatusOrStr
    """The verification status. One of the following:

    ``"VERIFIED"``: The information was successfully verified.

    ``"UNVERIFIED"``: The verification has not yet been performed.

    ``"NEEDS_INFO"``: The verification was attempted but could not be completed due to missing information.

    "``UNABLE_TO_VERIFY``": The verification was performed and the information could not be verified.

    ``"UNKNOWN"``: The verification status is unknown."""


class EmployerIncomeSummaryFieldStringDict(TypedDict):
    value: str
    verification_status: VerificationStatusOrStr
