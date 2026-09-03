from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignalWarning(SdkBaseModel):
    """Conveys information about the errors causing missing or stale bank data used to construct the
    ``/signal/evaluate`` scores and response"""

    warning_type: Optional[str] = UNSET
    """A broad categorization of the warning. Safe for programmatic use."""

    warning_code: Optional[str] = UNSET
    """The warning code identifies a specific kind of warning that pertains to the error causing bank data to be
    missing. Safe for programmatic use. For more details on warning codes, please refer to Plaid standard error codes
    documentation. If you receive the ``ITEM_LOGIN_REQUIRED`` warning, we recommend re-authenticating your user by
    implementing Link's update mode. This will guide your user to fix their credentials, allowing Plaid to start
    fetching data again for future requests."""

    warning_message: Optional[str] = UNSET
    """A developer-friendly representation of the warning type. This may change over time and is not safe for
    programmatic use."""


class SignalWarningDict(TypedDict):
    warning_type: NotRequired[str]
    warning_code: NotRequired[str]
    warning_message: NotRequired[str]
