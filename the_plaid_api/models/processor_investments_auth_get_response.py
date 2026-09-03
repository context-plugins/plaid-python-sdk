from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account import Account, AccountDict
from .holding import Holding, HoldingDict
from .investments_auth_account_details401_k import (
    InvestmentsAuthAccountDetails401K,
    InvestmentsAuthAccountDetails401KDict,
)
from .investments_auth_data_sources import InvestmentsAuthDataSources, InvestmentsAuthDataSourcesDict
from .investments_auth_get_numbers import InvestmentsAuthGetNumbers, InvestmentsAuthGetNumbersDict
from .investments_auth_owner import InvestmentsAuthOwner, InvestmentsAuthOwnerDict
from .security import Security, SecurityDict


class ProcessorInvestmentsAuthGetResponse(SdkBaseModel):
    """ProcessorInvestmentsAuthGetResponse defines the response schema for ``/processor/investments/auth/get``"""

    account: Account
    """A single account at a financial institution."""

    holdings: list[Holding]
    """The holdings belonging to the investment account. Details of the securities in the holdings are provided in the
    ``securities`` field."""

    securities: list[Security]
    """Objects describing the securities held in the account."""

    owners: list[InvestmentsAuthOwner]
    """Information about the account owners for the account."""

    numbers: InvestmentsAuthGetNumbers
    """Identifying information for transferring holdings to an investment account."""

    data_sources: InvestmentsAuthDataSources
    """Object with metadata pertaining to the source of data for the account numbers, owners, and holdings that are
    returned."""

    account_details_401k: Optional[list[InvestmentsAuthAccountDetails401K]] = UNSET
    """Additional information for accounts of 401k subtype."""

    is_investments_fallback_item: Optional[bool] = UNSET
    """When true, this field indicates that the Item's portfolio was manually created with the Investments Fallback
    flow."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorInvestmentsAuthGetResponseDict(TypedDict):
    account: Account | AccountDict
    holdings: list[Holding | HoldingDict]
    securities: list[Security | SecurityDict]
    owners: list[InvestmentsAuthOwner | InvestmentsAuthOwnerDict]
    numbers: InvestmentsAuthGetNumbers | InvestmentsAuthGetNumbersDict
    data_sources: InvestmentsAuthDataSources | InvestmentsAuthDataSourcesDict
    account_details_401k: NotRequired[list[InvestmentsAuthAccountDetails401K | InvestmentsAuthAccountDetails401KDict]]
    is_investments_fallback_item: NotRequired[bool]
    request_id: str
