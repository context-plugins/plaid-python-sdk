from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .holding import Holding, HoldingDict
from .investment_account import InvestmentAccount, InvestmentAccountDict
from .investments_auth_account_details401_k import (
    InvestmentsAuthAccountDetails401K,
    InvestmentsAuthAccountDetails401KDict,
)
from .investments_auth_data_sources import InvestmentsAuthDataSources, InvestmentsAuthDataSourcesDict
from .investments_auth_get_numbers import InvestmentsAuthGetNumbers, InvestmentsAuthGetNumbersDict
from .investments_auth_owner import InvestmentsAuthOwner, InvestmentsAuthOwnerDict
from .item import Item, ItemDict
from .security import Security, SecurityDict


class InvestmentsAuthGetResponse(SdkBaseModel):
    """InvestmentsAuthGetResponse defines the response schema for ``/investments/auth/get``"""

    accounts: list[InvestmentAccount]
    """The accounts for which data is being retrieved"""

    holdings: list[Holding]
    """The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings
    are provided in the ``securities`` field."""

    securities: list[Security]
    """Objects describing the securities held in the accounts associated with the Item."""

    owners: list[InvestmentsAuthOwner]
    """Information about the account owners for the accounts associated with the Item."""

    numbers: InvestmentsAuthGetNumbers
    """Identifying information for transferring holdings to an investment account."""

    data_sources: InvestmentsAuthDataSources
    """Object with metadata pertaining to the source of data for the account numbers, owners, and holdings that are
    returned."""

    account_details_401k: Optional[list[InvestmentsAuthAccountDetails401K]] = UNSET
    """Additional information for accounts of 401k subtype."""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class InvestmentsAuthGetResponseDict(TypedDict):
    accounts: list[InvestmentAccount | InvestmentAccountDict]
    holdings: list[Holding | HoldingDict]
    securities: list[Security | SecurityDict]
    owners: list[InvestmentsAuthOwner | InvestmentsAuthOwnerDict]
    numbers: InvestmentsAuthGetNumbers | InvestmentsAuthGetNumbersDict
    data_sources: InvestmentsAuthDataSources | InvestmentsAuthDataSourcesDict
    account_details_401k: NotRequired[list[InvestmentsAuthAccountDetails401K | InvestmentsAuthAccountDetails401KDict]]
    item: Item | ItemDict
    request_id: str
