from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Status2(SdkBaseModel):
    """The point at which the user exited the Link flow. One of the following values."""

    requires_questions: Optional[Any] = UNSET
    """User prompted to answer security questions"""

    requires_selections: Optional[Any] = UNSET
    """User prompted to answer multiple choice question(s)"""

    requires_code: Optional[Any] = UNSET
    """User prompted to provide a one-time passcode"""

    choose_device: Optional[Any] = UNSET
    """User prompted to select a device on which to receive a one-time passcode"""

    requires_credentials: Optional[Any] = UNSET
    """User prompted to provide credentials for the selected financial institution or has not yet selected a financial
    institution"""

    requires_account_selection: Optional[Any] = UNSET
    """User prompted to select one or more financial accounts to share"""

    requires_oauth: Optional[Any] = UNSET
    """User prompted to enter an OAuth flow"""

    institution_not_found: Optional[Any] = UNSET
    """User exited the Link flow after unsuccessfully (no results returned) searching for a financial institution"""

    institution_not_supported: Optional[Any] = UNSET
    """User exited the Link flow after discovering their selected institution is no longer supported by Plaid"""


class Status2Dict(TypedDict):
    requires_questions: NotRequired[Any]
    requires_selections: NotRequired[Any]
    requires_code: NotRequired[Any]
    choose_device: NotRequired[Any]
    requires_credentials: NotRequired[Any]
    requires_account_selection: NotRequired[Any]
    requires_oauth: NotRequired[Any]
    institution_not_found: NotRequired[Any]
    institution_not_supported: NotRequired[Any]
