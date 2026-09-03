from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sandbox_income_webhook_fire_request_webhook_code import SandboxIncomeWebhookFireRequestWebhookCodeOrStr
from .enums.verification_status3 import VerificationStatus3OrStr


class SandboxIncomeFireWebhookRequest(SdkBaseModel):
    """SandboxIncomeFireWebhookRequest defines the request schema for ``/sandbox/income/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    item_id: str
    """The Item ID associated with the verification."""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    webhook: str
    """The URL to which the webhook should be sent."""

    verification_status: Optional[VerificationStatus3OrStr] = UNSET
    """``VERIFICATION_STATUS_PROCESSING_COMPLETE``: The income verification status processing has completed. If the user
    uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the
    ``/income/verification/paystubs/get`` endpoint and check the document metadata to see which documents were
    successfully parsed.

    ``VERIFICATION_STATUS_PROCESSING_FAILED``: A failure occurred when attempting to process the verification
    documentation.

    ``VERIFICATION_STATUS_PENDING_APPROVAL``: (deprecated) The income verification has been sent to the user for
    review."""

    webhook_code: SandboxIncomeWebhookFireRequestWebhookCodeOrStr
    """The webhook codes that can be fired by this test endpoint."""


class SandboxIncomeFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    item_id: str
    user_id: NotRequired[str]
    webhook: str
    verification_status: NotRequired[VerificationStatus3OrStr]
    webhook_code: SandboxIncomeWebhookFireRequestWebhookCodeOrStr
