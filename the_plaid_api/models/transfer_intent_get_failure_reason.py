from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferIntentGetFailureReason(SdkBaseModel):
    """The reason for a failed transfer intent. Returned only if the transfer intent status is ``failed``. Null
    otherwise."""

    error_type: Optional[str] = UNSET
    """A broad categorization of the error."""

    error_code: Optional[str] = UNSET
    """A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being
    declined)."""

    error_message: Optional[str] = UNSET
    """A human-readable description of the code associated with a failed transfer intent."""


class TransferIntentGetFailureReasonDict(TypedDict):
    error_type: NotRequired[str]
    error_code: NotRequired[str]
    error_message: NotRequired[str]
