from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class AssetsErrorWebhook(SdkBaseModel):
    """Fired when Asset Report generation has failed. The resulting ``error`` will have an ``error_type`` of
    ``ASSET_REPORT_ERROR``."""

    webhook_type: str
    """``ASSETS``"""

    webhook_code: str
    """``ERROR``"""

    error: Error | None
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    asset_report_id: str
    """The ID associated with the Asset Report."""

    user_id: Optional[str] = UNSET
    """The ``user_id`` corresponding to the User ID the webhook has fired for."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class AssetsErrorWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: Error | ErrorDict | None
    asset_report_id: str
    user_id: NotRequired[str]
    environment: WebhookEnvironmentValuesOrStr
