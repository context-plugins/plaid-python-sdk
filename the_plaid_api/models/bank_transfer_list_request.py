from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.bank_transfer_direction import BankTransferDirectionOrStr


class BankTransferListRequest(SdkBaseModel):
    """Defines the request schema for ``/bank_transfer/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. ``2019-12-06T22:35:49Z``)"""

    count: Optional[int] = UNSET
    """The maximum number of bank transfers to return."""

    offset: Optional[int] = UNSET
    """The number of bank transfers to skip before returning results."""

    origination_account_id: OptionalNullable[str] = UNSET
    """Filter bank transfers to only those originated through the specified origination account."""

    direction: OptionalNullable[BankTransferDirectionOrStr] = UNSET
    """Indicates the direction of the transfer: ``outbound`` for API-initiated transfers, or ``inbound`` for payments
    received by the FBO account."""


class BankTransferListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int]
    offset: NotRequired[int]
    origination_account_id: NotRequired[str | None]
    direction: NotRequired[BankTransferDirectionOrStr | None]
