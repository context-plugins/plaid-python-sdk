from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.verify_smsdetails_status import VerifySmsdetailsStatusOrStr
from .smsverification import Smsverification, SmsverificationDict


class VerifySmsdetails(SdkBaseModel):
    """Additional information for the ``verify_sms`` step."""

    status: VerifySmsdetailsStatusOrStr
    """The outcome status for the associated Identity Verification attempt's ``verify_sms`` step. This field will always
    have the same value as ``steps.verify_sms``."""

    verifications: list[Smsverification]
    """An array where each entry represents a verification attempt for the ``verify_sms`` step. Each entry represents
    one user-submitted phone number. Phone number edits, and in some cases error handling due to edge cases like rate
    limiting, may generate additional verifications."""


class VerifySmsdetailsDict(TypedDict):
    status: VerifySmsdetailsStatusOrStr
    verifications: list[Smsverification | SmsverificationDict]
