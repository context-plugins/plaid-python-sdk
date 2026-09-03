from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .check_report_repairable_item import CheckReportRepairableItem, CheckReportRepairableItemDict
from .enums.products import ProductsOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr
from .error import Error, ErrorDict


class CraCheckReportFailedWebhook(SdkBaseModel):
    """Fired when a Check Report has failed to generate. To get more details, call ``/user/items/get`` and check for
    non-null ``error`` objects on the associated Items in the response. These ``error`` objects will contain more
    details on why the Item is in an error state and how to resolve it. After resolving the errors, you can try to
    re-generate the report."""

    webhook_type: str
    """``CHECK_REPORT``"""

    webhook_code: str
    """``CHECK_REPORT_FAILED``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    error: OptionalNullable[Error] = UNSET
    """Details on why the Check Report failed and how to resolve it."""

    repairable_items: Optional[list[CheckReportRepairableItem]] = UNSET
    """A list of Items that the end user can repair via Link `update mode <https://plaid.com/docs/link/update-mode>`__.
    Empty when no Item is user-repairable. After repairing these Items, call ``/cra/check_report/create`` to regenerate
    the report."""

    failed_products: Optional[list[ProductsOrStr]] = UNSET
    """Specifies a list of products that failed to generate for the report. Populated when generation was attempted and
    all requested products failed. Additional detail on what caused the failure can be found by calling the product /get
    endpoint."""

    item_ids: Optional[list[str | None]] = UNSET
    """A list of ``item_ids`` included in the Check Report. Access to this field is in closed beta."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CraCheckReportFailedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    error: NotRequired[Error | ErrorDict | None]
    repairable_items: NotRequired[list[CheckReportRepairableItem | CheckReportRepairableItemDict]]
    failed_products: NotRequired[list[ProductsOrStr]]
    item_ids: NotRequired[list[str | None]]
    environment: WebhookEnvironmentValuesOrStr
