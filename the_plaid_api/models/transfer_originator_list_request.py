from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferOriginatorListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/originator/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    count: int | None = 25
    """The maximum number of originators to return."""

    offset: int | None = 0
    """The number of originators to skip before returning results."""


class TransferOriginatorListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    count: NotRequired[int | None]
    offset: NotRequired[int | None]
