from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.payment_initiation_consent_status import PaymentInitiationConsentStatusOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class PaymentInitiationConsentStatusUpdateWebhook(SdkBaseModel):
    """Fired when the status of a payment consent has changed."""

    webhook_type: str
    """``PAYMENT_INITIATION``"""

    webhook_code: str
    """``CONSENT_STATUS_UPDATE``"""

    consent_id: str
    """The ``id`` for the consent being updated"""

    old_status: PaymentInitiationConsentStatusOrStr
    """The status of the payment consent.

    ``UNAUTHORISED``: Consent created, but requires user authorisation.

    ``REJECTED``: Consent authorisation was rejected by the bank.

    ``AUTHORISED``: Consent is active and ready to be used.

    ``REVOKED``: Consent has been revoked and can no longer be used.

    ``EXPIRED``: Consent is no longer valid."""

    new_status: PaymentInitiationConsentStatusOrStr
    """The status of the payment consent.

    ``UNAUTHORISED``: Consent created, but requires user authorisation.

    ``REJECTED``: Consent authorisation was rejected by the bank.

    ``AUTHORISED``: Consent is active and ready to be used.

    ``REVOKED``: Consent has been revoked and can no longer be used.

    ``EXPIRED``: Consent is no longer valid."""

    timestamp: RFC3339DateTime
    """The timestamp of the update, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class PaymentInitiationConsentStatusUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    consent_id: str
    old_status: PaymentInitiationConsentStatusOrStr
    new_status: PaymentInitiationConsentStatusOrStr
    timestamp: RFC3339DateTime
    error: NotRequired[ErrorDict | None]
    environment: WebhookEnvironmentValuesOrStr
