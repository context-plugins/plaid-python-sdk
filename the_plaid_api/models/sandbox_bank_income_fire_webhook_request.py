from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sandbox_bank_income_webhook_fire_request_webhook_code import (
    SandboxBankIncomeWebhookFireRequestWebhookCodeOrStr,
)
from .sandbox_bank_income_webhook_fire_request_webhook_fields import (
    SandboxBankIncomeWebhookFireRequestWebhookFields,
    SandboxBankIncomeWebhookFireRequestWebhookFieldsDict,
)


class SandboxBankIncomeFireWebhookRequest(SdkBaseModel):
    """SandboxBankIncomeFireWebhookRequest defines the request schema for ``/sandbox/bank_income/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    webhook_override: Optional[str] = UNSET
    """The URL to which the webhook should be sent. If provided, this will override the URL set in the dashboard."""

    webhook_code: SandboxBankIncomeWebhookFireRequestWebhookCodeOrStr
    """The webhook codes this endpoint can be used to test"""

    webhook_fields: SandboxBankIncomeWebhookFireRequestWebhookFields
    """Optional fields which will be populated in the simulated webhook"""


class SandboxBankIncomeFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    webhook_override: NotRequired[str]
    webhook_code: SandboxBankIncomeWebhookFireRequestWebhookCodeOrStr
    webhook_fields: SandboxBankIncomeWebhookFireRequestWebhookFieldsDict
