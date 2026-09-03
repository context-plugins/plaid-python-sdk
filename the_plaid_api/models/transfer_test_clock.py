from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class TransferTestClock(SdkBaseModel):
    """Defines the test clock for a transfer."""

    test_clock_id: str
    """Plaid's unique identifier for a test clock. This field is only populated in the Sandbox environment, and only if
    a ``test_clock_id`` was included in the ``/transfer/recurring/create`` request. For more details, see `Simulating
    recurring transfers <https://plaid.com/docs/transfer/sandbox/#simulating-recurring-transfers>`__."""

    virtual_time: RFC3339DateTime
    """The virtual timestamp on the test clock. This will be of the form ``2006-01-02T15:04:05Z``."""


class TransferTestClockDict(TypedDict):
    test_clock_id: str
    virtual_time: RFC3339DateTime
