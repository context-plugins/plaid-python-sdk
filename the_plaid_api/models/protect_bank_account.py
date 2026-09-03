from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ProtectBankAccount(SdkBaseModel):
    """Bank account information associated with the incident."""

    account_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for the account."""

    account_number: OptionalNullable[str] = UNSET
    """Full account number of the bank account."""

    routing_number: OptionalNullable[str] = UNSET
    """Routing number of the bank account. Must be present if ``account_number`` is present."""


class ProtectBankAccountDict(TypedDict):
    account_id: NotRequired[str | None]
    account_number: NotRequired[str | None]
    routing_number: NotRequired[str | None]
