from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SignalPersonName(SdkBaseModel):
    """The user's legal name"""

    prefix: OptionalNullable[str] = UNSET
    """The user's name prefix (e.g. "Mr.")"""

    given_name: OptionalNullable[str] = UNSET
    """The user's given name. If the user has a one-word name, it should be provided in this field."""

    middle_name: OptionalNullable[str] = UNSET
    """The user's middle name"""

    family_name: OptionalNullable[str] = UNSET
    """The user's family name / surname"""

    suffix: OptionalNullable[str] = UNSET
    """The user's name suffix (e.g. "II")"""


class SignalPersonNameDict(TypedDict):
    prefix: NotRequired[str | None]
    given_name: NotRequired[str | None]
    middle_name: NotRequired[str | None]
    family_name: NotRequired[str | None]
    suffix: NotRequired[str | None]
