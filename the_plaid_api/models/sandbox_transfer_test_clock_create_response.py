from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_test_clock import TransferTestClock, TransferTestClockDict


class SandboxTransferTestClockCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/transfer/test_clock/create``"""

    test_clock: TransferTestClock
    """Defines the test clock for a transfer."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransferTestClockCreateResponseDict(TypedDict):
    test_clock: TransferTestClockDict
    request_id: str
