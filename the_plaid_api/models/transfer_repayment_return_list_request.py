from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferRepaymentReturnListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/repayment/return/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    repayment_id: str
    """Identifier of the repayment to query."""

    count: OptionalNullable[int] = UNSET
    """The maximum number of repayments to return."""

    offset: Optional[int] = UNSET
    """The number of repayments to skip before returning results."""


class TransferRepaymentReturnListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    repayment_id: str
    count: NotRequired[int | None]
    offset: NotRequired[int]
