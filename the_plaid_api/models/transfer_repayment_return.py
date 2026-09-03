from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferRepaymentReturn(SdkBaseModel):
    """Represents a return on a Guaranteed ACH transfer that is included in the specified repayment."""

    transfer_id: str
    """The unique identifier of the guaranteed transfer that was returned."""

    event_id: int
    """The unique identifier of the corresponding ``returned`` transfer event."""

    amount: str
    """The value of the returned transfer."""

    iso_currency_code: str
    """The currency of the repayment, e.g. "USD"."""


class TransferRepaymentReturnDict(TypedDict):
    transfer_id: str
    event_id: int
    amount: str
    iso_currency_code: str
