from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TransferRecurringListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/recurring/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The start ``created`` datetime of recurring transfers to list. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end ``created`` datetime of recurring transfers to list. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    count: int = 25
    """The maximum number of recurring transfers to return."""

    offset: int = 0
    """The number of recurring transfers to skip before returning results."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Filter recurring transfers to only those with the specified ``funding_account_id``."""


class TransferRecurringListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int]
    offset: NotRequired[int]
    funding_account_id: NotRequired[str | None]
