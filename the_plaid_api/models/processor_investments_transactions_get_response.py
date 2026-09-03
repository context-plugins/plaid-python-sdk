from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .investment_account import InvestmentAccount, InvestmentAccountDict
from .investment_transaction import InvestmentTransaction, InvestmentTransactionDict
from .security import Security, SecurityDict


class ProcessorInvestmentsTransactionsGetResponse(SdkBaseModel):
    """ProcessorInvestmentsTransactionsGetResponse defines the response schema for
    ``/processor/investments/transactions/get``"""

    account: InvestmentAccount
    """A single account at a financial institution, with additional investment-specific balance information."""

    investment_transactions: list[InvestmentTransaction]
    """An array containing investment transactions from the account. Investments transactions are returned in reverse
    chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned
    is determined by the ``count`` parameter."""

    securities: list[Security]
    """All securities for which there is a corresponding transaction being fetched."""

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


class ProcessorInvestmentsTransactionsGetResponseDict(TypedDict):
    account: InvestmentAccount | InvestmentAccountDict
    investment_transactions: list[InvestmentTransaction | InvestmentTransactionDict]
    securities: list[Security | SecurityDict]
    total_investment_transactions: int
    request_id: str
    is_investments_fallback_item: NotRequired[bool]
