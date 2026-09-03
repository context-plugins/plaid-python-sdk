from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class SandboxTransferTestClockAdvanceRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/test_clock/advance``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    test_clock_id: str
    """Plaid's unique identifier for a test clock. This field is only populated in the Sandbox environment, and only if
    a ``test_clock_id`` was included in the ``/transfer/recurring/create`` request. For more details, see `Simulating
    recurring transfers <https://plaid.com/docs/transfer/sandbox/#simulating-recurring-transfers>`__."""

    new_virtual_time: RFC3339DateTime
    """The virtual timestamp on the test clock. This will be of the form ``2006-01-02T15:04:05Z``."""


class SandboxTransferTestClockAdvanceRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    test_clock_id: str
    new_virtual_time: RFC3339DateTime
