from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CraUserCheckReportReadyWebhook(SdkBaseModel):
    """Fired when the Check Report is ready to be retrieved. Once this webhook has fired, the report will be available
    to retrieve for 24 hours."""

    webhook_type: str
    """``CHECK_REPORT``"""

    webhook_code: str
    """``USER_CHECK_REPORT_READY``"""

    user_id: str
    """The ``user_id`` associated with the user whose data is being requested. This is received by calling
    ``/user/create``."""

    successful_products: Optional[list[ProductsOrStr]] = UNSET
    """Specifies a list of products that have successfully been generated for the report."""

    failed_products: Optional[list[ProductsOrStr]] = UNSET
    """Specifies a list of products that have failed to generate for the report. Additional detail on what caused the
    failure can be found by calling the product /get endpoint."""

    item_ids: Optional[list[str | None]] = UNSET
    """A list of ``item_ids`` included in the Check Report. Access to this field is in closed beta."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CraUserCheckReportReadyWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    successful_products: NotRequired[list[ProductsOrStr]]
    failed_products: NotRequired[list[ProductsOrStr]]
    item_ids: NotRequired[list[str | None]]
    environment: WebhookEnvironmentValuesOrStr
