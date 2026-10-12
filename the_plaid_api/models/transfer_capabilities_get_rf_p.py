from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TransferCapabilitiesGetRfP(SdkBaseModel):
    """Contains the supported service types in RfP"""

    debit: bool = False
    """When ``true``, the linked Item's institution supports RfP debit transfer."""

    max_amount: OptionalNullable[str] = UNSET
    """The maximum amount (decimal string with two digits of precision e.g. "10.00") for originating RfP transfers with
    the given institution."""

    iso_currency_code: OptionalNullable[str] = UNSET
    """The currency of the ``max_amount``, e.g. "USD"."""


class TransferCapabilitiesGetRfPDict(TypedDict):
    debit: NotRequired[bool]
    max_amount: NotRequired[str | None]
    iso_currency_code: NotRequired[str | None]
