from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SandboxTransferTestClockCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/test_clock/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    virtual_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The virtual timestamp on the test clock. If not provided, the current timestamp will be used. This will be of the
    form ``2006-01-02T15:04:05Z``."""


class SandboxTransferTestClockCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    virtual_time: NotRequired[RFC3339DateTime | None]
