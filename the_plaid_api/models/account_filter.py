from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountFilter(SdkBaseModel):
    """Enumerates the account subtypes that the application wishes for the user to be able to select from. For more
    details refer to Plaid documentation on account filters."""

    depository: Optional[list[str]] = UNSET
    """A list of account subtypes to be filtered."""

    credit: Optional[list[str]] = UNSET
    """A list of account subtypes to be filtered."""

    loan: Optional[list[str]] = UNSET
    """A list of account subtypes to be filtered."""

    investment: Optional[list[str]] = UNSET
    """A list of account subtypes to be filtered."""


class AccountFilterDict(TypedDict):
    depository: NotRequired[list[str]]
    credit: NotRequired[list[str]]
    loan: NotRequired[list[str]]
    investment: NotRequired[list[str]]
