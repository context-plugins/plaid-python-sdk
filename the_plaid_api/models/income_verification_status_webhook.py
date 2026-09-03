from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class IncomeVerificationStatusWebhook(SdkBaseModel):
    """Fired when the status of an income verification instance has changed. This webhook is fired for both the Document
    and Payroll Income flows, but not the Bank Income flow. It will typically take several minutes for this webhook to
    fire after the end user has uploaded their documents in the Document Income flow."""

    webhook_type: str
    """``"INCOME"``"""

    webhook_code: str
    """``INCOME_VERIFICATION``"""

    item_id: str
    """The Item ID associated with the verification."""

    user_id: Optional[str] = UNSET
    """The Plaid ``user_id`` of the User associated with this webhook, warning, or error."""

    verification_status: str
    """``VERIFICATION_STATUS_PROCESSING_COMPLETE``: The income verification processing has completed. This indicates
    that the documents have been parsed successfully or that the documents were not parsable. If the user uploaded
    multiple documents, this webhook will fire when all documents have finished processing. Call the
    ``/credit/payroll_income/get`` endpoint and check the document metadata to see which documents were successfully
    parsed.

    ``VERIFICATION_STATUS_PROCESSING_FAILED``: An unexpected internal error occurred when attempting to process the
    verification documentation.

    ``VERIFICATION_STATUS_PENDING_APPROVAL``: (deprecated) The income verification has been sent to the user for
    review."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class IncomeVerificationStatusWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    user_id: NotRequired[str]
    verification_status: str
    environment: WebhookEnvironmentValuesOrStr
