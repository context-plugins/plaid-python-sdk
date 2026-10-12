from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TransferListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start ``created`` datetime of transfers to list. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end ``created`` datetime of transfers to list. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    count: int = 25
    """The maximum number of transfers to return."""

    offset: int = 0
    """The number of transfers to skip before returning results."""

    origination_account_id: OptionalNullable[str] = UNSET
    """Filter transfers to only those originated through the specified origination account."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Filter transfers to only those with the specified originator client."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Filter transfers to only those with the specified ``funding_account_id``."""


class TransferListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int]
    offset: NotRequired[int]
    origination_account_id: NotRequired[str | None]
    originator_client_id: NotRequired[str | None]
    funding_account_id: NotRequired[str | None]
