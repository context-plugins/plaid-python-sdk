from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.partner_end_customer_oauth_status_updated_values import PartnerEndCustomerOauthStatusUpdatedValuesOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class PartnerEndCustomerOauthStatusUpdatedWebhook(SdkBaseModel):
    """The webhook of type ``PARTNER`` and code ``END_CUSTOMER_OAUTH_STATUS_UPDATED`` will be fired when a partner's end
    customer has an update on their OAuth registration status with an institution."""

    webhook_type: str
    """``PARTNER``"""

    webhook_code: str
    """``END_CUSTOMER_OAUTH_STATUS_UPDATED``"""

    end_customer_client_id: str
    """The client ID of the end customer"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""

    institution_id: str
    """The institution ID"""

    institution_name: str
    """The institution name"""

    status: PartnerEndCustomerOauthStatusUpdatedValuesOrStr
    """The OAuth status of the update"""


class PartnerEndCustomerOauthStatusUpdatedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    end_customer_client_id: str
    environment: WebhookEnvironmentValuesOrStr
    institution_id: str
    institution_name: str
    status: PartnerEndCustomerOauthStatusUpdatedValuesOrStr
