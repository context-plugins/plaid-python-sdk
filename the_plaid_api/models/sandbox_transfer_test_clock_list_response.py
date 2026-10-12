from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_test_clock import TransferTestClock, TransferTestClockDict


class SandboxTransferTestClockListResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/transfer/test_clock/list``"""

    test_clocks: list[TransferTestClock]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxTransferTestClockListResponseDict(TypedDict):
    test_clocks: list[TransferTestClockDict]
    request_id: str
