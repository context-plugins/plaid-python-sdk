from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.asset_report_type import AssetReportTypeOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class AssetsProductReadyWebhook(SdkBaseModel):
    """Fired when the Asset Report has been generated and ``/asset_report/get`` is ready to be called. If you attempt to
    retrieve an Asset Report before this webhook has fired, you'll receive a response with the HTTP status code 400 and
    a Plaid error code of ``PRODUCT_NOT_READY``."""

    webhook_type: str
    """``ASSETS``"""

    webhook_code: str
    """``PRODUCT_READY``"""

    asset_report_id: str
    """The ``asset_report_id`` corresponding to the Asset Report the webhook has fired for."""

    user_id: Optional[str] = UNSET
    """The ``user_id`` corresponding to the User ID the webhook has fired for."""

    report_type: Optional[AssetReportTypeOrStr] = UNSET
    """Indicates either a Fast Asset Report, which will contain only current identity and balance information, or a Full
    Asset Report, which will also contain historical balance information and transaction data."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class AssetsProductReadyWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    asset_report_id: str
    user_id: NotRequired[str]
    report_type: NotRequired[AssetReportTypeOrStr]
    environment: WebhookEnvironmentValuesOrStr
