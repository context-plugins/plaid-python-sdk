from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserAccountItem(SdkBaseModel):
    """An Item created during a Layer authorization session."""

    item_id: Optional[str] = UNSET
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    access_token: Optional[str] = UNSET
    """The access token associated with the Item for which data is being requested."""


class UserAccountItemDict(TypedDict):
    item_id: NotRequired[str]
    access_token: NotRequired[str]
