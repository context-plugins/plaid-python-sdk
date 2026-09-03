from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .investment_account import InvestmentAccount, InvestmentAccountDict
from .investment_transaction import InvestmentTransaction, InvestmentTransactionDict
from .item import Item, ItemDict
from .security import Security, SecurityDict


class InvestmentsTransactionsGetResponse(SdkBaseModel):
    """InvestmentsTransactionsGetResponse defines the response schema for ``/investments/transactions/get``"""

    item: Item
    """Metadata about the Item."""

    accounts: list[InvestmentAccount]
    """The accounts for which transaction history is being fetched."""

    securities: list[Security]
    """All securities for which there is a corresponding transaction being fetched."""

    investment_transactions: list[InvestmentTransaction]
    """The transactions being fetched"""

    total_investment_transactions: int
    """The total number of transactions available within the date range specified. If ``total_investment_transactions``
    is larger than the size of the ``transactions`` array, more transactions are available and can be fetched via
    manipulating the ``offset`` parameter."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    is_investments_fallback_item: Optional[bool] = UNSET
    """When true, this field indicates that the Item's portfolio was manually created with the Investments Fallback
    flow."""


class InvestmentsTransactionsGetResponseDict(TypedDict):
    item: Item | ItemDict
    accounts: list[InvestmentAccount | InvestmentAccountDict]
    securities: list[Security | SecurityDict]
    investment_transactions: list[InvestmentTransaction | InvestmentTransactionDict]
    total_investment_transactions: int
    request_id: str
    is_investments_fallback_item: NotRequired[bool]
