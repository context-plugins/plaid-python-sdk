from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferRefundCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/refund/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: str
    """The ID of the transfer to refund."""

    amount: str
    """The amount of the refund (decimal string with two digits of precision e.g. "10.00")."""

    idempotency_key: str
    """A random key provided by the client, per unique refund. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create a refund fails due to a network connection error, you can retry the request with
    the same idempotency key to guarantee that only a single refund is created."""


class TransferRefundCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: str
    amount: str
    idempotency_key: str
