from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_bank_income_account_metadata import CraBankIncomeAccountMetadata, CraBankIncomeAccountMetadataDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr


class CraVerificationIncomeAccount(SdkBaseModel):
    """Account information within the Home Lending Income Report."""

    account_id: str
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
    """The name of the account, either assigned by the user or by the financial institution itself."""

    official_name: str | None
    """The official name of the account as given by the financial institution."""

    subtype: AccountSubtypeOrStr | None
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    type_: AccountTypeOrStr = Field(alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""


class CraVerificationIncomeAccountDict(TypedDict):
    account_id: str
    mask: str | None
    metadata: CraBankIncomeAccountMetadataDict
    name: str
    official_name: str | None
    subtype: AccountSubtypeOrStr | None
    type_: AccountTypeOrStr
