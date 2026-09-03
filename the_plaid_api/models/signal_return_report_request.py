from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SignalReturnReportRequest(SdkBaseModel):
    """SignalReturnReportRequest defines the request schema for ``/signal/return/report``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_transaction_id: str
    """Must be the same as the ``client_transaction_id`` supplied when calling ``/signal/evaluate``."""

    return_code: str
    """Must be a valid ACH return code (e.g. "R01")

    If formatted incorrectly, this will result in an https://plaid.com/docs/errors/invalid-request/#invalid_field
    error."""

    returned_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Date and time when you receive the returns from your payment processors, in ISO 8601 format
    (``YYYY-MM-DDTHH:mm:ssZ``)."""


class SignalReturnReportRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_transaction_id: str
    return_code: str
    returned_at: NotRequired[RFC3339DateTime | None]
