from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferFailure(SdkBaseModel):
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""

    failure_code: OptionalNullable[str] = UNSET
    """The failure code, e.g. ``R01``. A failure code will be provided if and only if the transfer status is
    ``returned``. See `ACH return codes <https://plaid.com/docs/errors/transfer/#ach-return-codes>`__ for a full listing
    of ACH return codes and `RTP/RfP error codes <https://plaid.com/docs/errors/transfer/#rtprfp-error-codes>`__ for RTP
    error codes."""

    ach_return_code: OptionalNullable[str] = UNSET
    """The ACH return code, e.g. ``R01``. A return code will be provided if and only if the transfer status is
    ``returned``. For a full listing of ACH return codes, see `Transfer errors
    <https://plaid.com/docs/errors/transfer/#ach-return-codes>`__."""

    description: Optional[str] = UNSET
    """A human-readable description of the reason for the failure or reversal."""


class TransferFailureDict(TypedDict):
    failure_code: NotRequired[str | None]
    ach_return_code: NotRequired[str | None]
    description: NotRequired[str]
