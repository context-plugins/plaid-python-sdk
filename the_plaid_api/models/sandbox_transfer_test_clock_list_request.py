from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SandboxTransferTestClockListRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/test_clock/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_virtual_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The start virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    end_virtual_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The end virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e.
    ``2019-12-06T22:35:49Z``)"""

    count: int | None = 25
    """The maximum number of test clocks to return."""

    offset: int = 0
    """The number of test clocks to skip before returning results."""


class SandboxTransferTestClockListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_virtual_time: NotRequired[RFC3339DateTime | None]
    end_virtual_time: NotRequired[RFC3339DateTime | None]
    count: NotRequired[int | None]
    offset: NotRequired[int]
