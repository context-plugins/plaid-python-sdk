from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RecaptchaRequiredError(SdkBaseModel):
    """The request was flagged by Plaid's fraud system and requires additional verification to ensure the user is not a
    bot."""

    error_type: str
    """``RECAPTCHA_ERROR``"""

    error_code: str
    """``RECAPTCHA_REQUIRED``"""

    display_message: str | None
    http_code: int
    """400"""

    link_user_experience: Optional[str] = UNSET
    """Your user will be prompted to solve a Google reCAPTCHA challenge in the Link Recaptcha pane. If they solve the
    challenge successfully, the user's request is resubmitted and they are directed to the next Item creation step."""

    common_causes: Optional[str] = UNSET
    """Plaid's fraud system detects abusive traffic and considers a variety of parameters throughout Item creation
    requests. When a request is considered risky or possibly fraudulent, Link presents a reCAPTCHA for the user to
    solve."""

    troubleshooting_steps: Optional[str] = UNSET
    """Link will automatically guide your user through reCAPTCHA verification. As a general rule, we recommend
    instrumenting basic fraud monitoring to detect and protect your website from spam and abuse.

    If your user cannot verify their session, please submit a support ticket with the following identifiers:
    ``link_session_id`` or ``request_id``"""


class RecaptchaRequiredErrorDict(TypedDict):
    error_type: str
    error_code: str
    display_message: str | None
    http_code: int
    link_user_experience: NotRequired[str]
    common_causes: NotRequired[str]
    troubleshooting_steps: NotRequired[str]
