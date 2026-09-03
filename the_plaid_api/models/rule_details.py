from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RuleDetails(SdkBaseModel):
    """Rules are run in numerical order. The first rule with a logic match is triggered. These are the details of that
    rule."""

    internal_note: Optional[str] = UNSET
    """An optional message attached to the triggered rule, defined within the Dashboard, for your internal use. Useful
    for debugging, such as "Account appears to be closed."
    """

    custom_action_key: Optional[str] = UNSET
    """A string key, defined within the Dashboard, used to trigger programmatic behavior for a certain result. For
    instance, you could optionally choose to define a "3-day-hold" ``custom_action_key`` for an ACCEPT result."""


class RuleDetailsDict(TypedDict):
    internal_note: NotRequired[str]
    custom_action_key: NotRequired[str]
