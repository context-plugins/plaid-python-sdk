from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .holding import Holding, HoldingDict
from .investment_account import InvestmentAccount, InvestmentAccountDict
from .security import Security, SecurityDict


class ProcessorInvestmentsHoldingsGetResponse(SdkBaseModel):
    """ProcessorInvestmentsHoldingsGetResponse defines the response schema for
    ``/processor/investments/holdings/get``"""

    account: InvestmentAccount
    """A single account at a financial institution, with additional investment-specific balance information."""

    holdings: list[Holding]
    """The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings
    are provided in the ``securities`` field."""

    securities: list[Security]
    """Objects describing the securities held in the account."""

    is_investments_fallback_item: Optional[bool] = UNSET
    """When true, this field indicates that the Item's portfolio was manually created with the Investments Fallback
    flow."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorInvestmentsHoldingsGetResponseDict(TypedDict):
    account: InvestmentAccountDict
    holdings: list[HoldingDict]
    securities: list[SecurityDict]
    is_investments_fallback_item: NotRequired[bool]
    request_id: NotRequired[str]
