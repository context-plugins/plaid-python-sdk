from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxPaymentSimulateRequest(SdkBaseModel):
    """SandboxPaymentSimulateRequest defines the request schema for ``/sandbox/payment/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    payment_id: str
    """The ID of the payment to simulate"""

    webhook: str
    """The webhook url to use for any payment events triggered by the simulated status change."""

    status: str
    """The status to set the payment to.

    Valid statuses include:
    - ``PAYMENT_STATUS_INITIATED``
    - ``PAYMENT_STATUS_INSUFFICIENT_FUNDS``
    - ``PAYMENT_STATUS_FAILED``
    - ``PAYMENT_STATUS_EXECUTED``
    - ``PAYMENT_STATUS_SETTLED``
    - ``PAYMENT_STATUS_CANCELLED``
    - ``PAYMENT_STATUS_REJECTED``"""


class SandboxPaymentSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    payment_id: str
    webhook: str
    status: str
