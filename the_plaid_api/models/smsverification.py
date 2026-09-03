from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.smsverification_status import SmsverificationStatusOrStr


class Smsverification(SdkBaseModel):
    """Additional information for the individual SMS verification."""

    status: SmsverificationStatusOrStr
    """The outcome status for the individual SMS verification."""

    attempt: int
    """The attempt field begins with 1 and increments with each subsequent SMS verification."""

    phone_number: str | None
    """A phone number in E.164 format."""

    delivery_attempt_count: int
    """The number of delivery attempts made within the verification to send the SMS code to the user. Each delivery
    attempt represents the user taking action from the front end UI to request creation and delivery of a new SMS
    verification code, or to resend an existing SMS verification code. There is a limit of 3 delivery attempts per
    verification."""

    solve_attempt_count: int
    """The number of attempts made by the user within the verification to verify the SMS code by entering it into the
    front end UI. There is a limit of 3 solve attempts per verification."""

    initially_sent_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    last_sent_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    redacted_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""


class SmsverificationDict(TypedDict):
    status: SmsverificationStatusOrStr
    attempt: int
    phone_number: str | None
    delivery_attempt_count: int
    solve_attempt_count: int
    initially_sent_at: RFC3339DateTime | None
    last_sent_at: RFC3339DateTime | None
    redacted_at: RFC3339DateTime | None
