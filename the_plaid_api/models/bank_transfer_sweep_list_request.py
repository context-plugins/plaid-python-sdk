from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class BankTransferSweepListRequest(SdkBaseModel):
    """BankTransferSweepListRequest defines the request schema for ``/bank_transfer/sweep/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    origination_account_id: OptionalNullable[str] = UNSET
    """If multiple origination accounts are available, ``origination_account_id`` must be used to specify the account
    that the sweeps belong to."""

    start_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The start ``created`` datetime of sweeps to return (RFC 3339 format)."""

    end_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end ``created`` datetime of sweeps to return (RFC 3339 format)."""

    count: int | None = 25
    """The maximum number of sweeps to return."""


class BankTransferSweepListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    origination_account_id: NotRequired[str | None]
    start_time: NotRequired[RFC3339DateTime | None]
    end_time: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int | None]
