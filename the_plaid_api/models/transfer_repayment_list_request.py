from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TransferRepaymentListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/repayment/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start ``created`` datetime of repayments to return (RFC 3339 format)."""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end ``created`` datetime of repayments to return (RFC 3339 format)."""

    count: OptionalNullable[int] = UNSET
    """The maximum number of repayments to return."""

    offset: Optional[int] = UNSET
    """The number of repayments to skip before returning results."""


class TransferRepaymentListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int | None]
    offset: NotRequired[int]
