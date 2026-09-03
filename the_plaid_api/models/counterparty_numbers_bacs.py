from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CounterpartyNumbersBacs(SdkBaseModel):
    """Identifying information for a UK bank account via Bacs."""

    account: OptionalNullable[str] = UNSET
    """The Bacs account number for the account."""

    sort_code: OptionalNullable[str] = UNSET
    """The Bacs sort code for the account."""


class CounterpartyNumbersBacsDict(TypedDict):
    account: NotRequired[str | None]
    sort_code: NotRequired[str | None]
