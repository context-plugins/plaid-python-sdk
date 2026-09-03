from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class BankTransferSweep(SdkBaseModel):
    """BankTransferSweep describes a sweep transfer."""

    id: str
    """Identifier of the sweep."""

    created_at: RFC3339DateTime
    """The datetime when the sweep occurred, in RFC 3339 format."""

    amount: str
    """The amount of the sweep."""

    iso_currency_code: str
    """The currency of the sweep, e.g. "USD"."""


class BankTransferSweepDict(TypedDict):
    id: str
    created_at: RFC3339DateTime
    amount: str
    iso_currency_code: str
