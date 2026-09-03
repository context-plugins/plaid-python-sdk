from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .holding import Holding, HoldingDict
from .investment_account import InvestmentAccount, InvestmentAccountDict
from .item import Item, ItemDict
from .security import Security, SecurityDict


class InvestmentsHoldingsGetResponse(SdkBaseModel):
    """InvestmentsHoldingsGetResponse defines the response schema for ``/investments/holdings/get``"""

    accounts: list[InvestmentAccount]
    """The accounts associated with the Item"""

    holdings: list[Holding]
    """The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings
    are provided in the ``securities`` field."""

    securities: list[Security]
    """Objects describing the securities held in the accounts associated with the Item."""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    is_investments_fallback_item: Optional[bool] = UNSET
    """When true, this field indicates that the Item's portfolio was manually created with the Investments Fallback
    flow."""


class InvestmentsHoldingsGetResponseDict(TypedDict):
    accounts: list[InvestmentAccount | InvestmentAccountDict]
    holdings: list[Holding | HoldingDict]
    securities: list[Security | SecurityDict]
    item: Item | ItemDict
    request_id: str
    is_investments_fallback_item: NotRequired[bool]
