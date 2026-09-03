from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BankTransfersEventsUpdateWebhookForAuth(SdkBaseModel):
    """Fired when new ACH events are available. To begin receiving this webhook, you must first register your webhook
    listener endpoint via the `webhooks page in the Dashboard <https://dashboard.plaid.com/team/webhooks>`__. The
    ``BANK_TRANSFERS_EVENTS_UPDATE`` webhook can be used to track the progress of ACH transfers used in `micro-deposit
    verification <https://plaid.com/docs/auth/coverage/microdeposit-events/>`__. Receiving this webhook indicates you
    should fetch the new events from ``/bank_transfer/event/sync``. Note that `Transfer
    <https://plaid.com/docs/transfer>`__ customers should use Transfer webhooks instead of using
    ``BANK_TRANSFERS_EVENTS_UPDATE``; see `micro-deposit events documentation
    <https://plaid.com/docs/auth/coverage/microdeposit-events/>`__ for more details."""

    webhook_type: str
    """``BANK_TRANSFERS``"""

    webhook_code: str
    """``BANK_TRANSFERS_EVENTS_UPDATE``"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BankTransfersEventsUpdateWebhookForAuthDict(TypedDict):
    webhook_type: str
    webhook_code: str
    environment: WebhookEnvironmentValuesOrStr
