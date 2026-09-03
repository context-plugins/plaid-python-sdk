from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SweepFailure(SdkBaseModel):
    """The failure reason if the status for a sweep is ``"failed"`` or ``"returned"``. Null value otherwise."""

    failure_code: OptionalNullable[str] = UNSET
    """The failure code, e.g. ``R01``. A failure code will be provided if and only if the sweep status is ``returned``.
    See `ACH return codes <https://plaid.com/docs/errors/transfer/#ach-return-codes>`__ for a full listing of ACH return
    codes and `RTP/RfP error codes <https://plaid.com/docs/errors/transfer/#rtprfp-error-codes>`__ for RTP error
    codes."""

    description: OptionalNullable[str] = UNSET
    """A human-readable description of the reason for the failure or reversal."""


class SweepFailureDict(TypedDict):
    failure_code: NotRequired[str | None]
    description: NotRequired[str | None]
