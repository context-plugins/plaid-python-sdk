from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_bank_income_account_metadata import CraBankIncomeAccountMetadata, CraBankIncomeAccountMetadataDict
from .enums.depository_account_subtype import DepositoryAccountSubtypeOrStr
from .owner import Owner, OwnerDict


class CraBankIncomeAccount(SdkBaseModel):
    """The Item's bank accounts that have the selected data."""

    account_id: Optional[str] = UNSET
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    metadata: CraBankIncomeAccountMetadata
    """An object containing metadata about the extracted account."""

    name: str
    """The name of the bank account."""

    official_name: str | None
    """The official name of the bank account."""

    subtype: DepositoryAccountSubtypeOrStr
    """Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository>`__."""

    type_: Literal["depository"] = Field(default="depository", alias="type")
    """The account type. This will always be ``depository``."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners. Identity information is optional,
    so field may return an empty array."""


class CraBankIncomeAccountDict(TypedDict):
    account_id: NotRequired[str]
    mask: str | None
    metadata: CraBankIncomeAccountMetadata | CraBankIncomeAccountMetadataDict
    name: str
    official_name: str | None
    subtype: DepositoryAccountSubtypeOrStr
    type_: NotRequired[Literal["depository"]]
    owners: list[Owner | OwnerDict]
