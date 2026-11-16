from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.verify_sms_details_status import VerifySmsDetailsStatusOrStr
from .sms_verification import SmsVerification, SmsVerificationDict


class VerifySmsDetails(SdkBaseModel):
    """Additional information for the ``verify_sms`` step."""

    status: VerifySmsDetailsStatusOrStr
    """The outcome status for the associated Identity Verification attempt's ``verify_sms`` step. This field will always
    have the same value as ``steps.verify_sms``."""

    verifications: list[SmsVerification]
    """An array where each entry represents a verification attempt for the ``verify_sms`` step. Each entry represents
    one user-submitted phone number. Phone number edits, and in some cases error handling due to edge cases like rate
    limiting, may generate additional verifications."""


class VerifySmsDetailsDict(TypedDict):
    status: VerifySmsDetailsStatusOrStr
    verifications: list[SmsVerificationDict]
