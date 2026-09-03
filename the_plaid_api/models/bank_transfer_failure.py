from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BankTransferFailure(SdkBaseModel):
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""

    ach_return_code: OptionalNullable[str] = UNSET
    """The ACH return code, e.g. ``R01``. A return code will be provided if and only if the transfer status is
    ``reversed``. For a full listing of ACH return codes, see `Bank Transfers errors
    <https://plaid.com/docs/errors/bank-transfers/#ach-return-codes>`__."""

    description: Optional[str] = UNSET
    """A human-readable description of the reason for the failure or reversal."""


class BankTransferFailureDict(TypedDict):
    ach_return_code: NotRequired[str | None]
    description: NotRequired[str]
