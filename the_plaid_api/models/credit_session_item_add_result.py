from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditSessionItemAddResult(SdkBaseModel):
    """The details of an Item add in Link."""

    public_token: Optional[str] = UNSET
    """Returned once a user has successfully linked their Item."""

    item_id: Optional[str] = UNSET
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    institution_id: Optional[str] = UNSET
    """The Plaid Institution ID associated with the Item."""


class CreditSessionItemAddResultDict(TypedDict):
    public_token: NotRequired[str]
    item_id: NotRequired[str]
    institution_id: NotRequired[str]
