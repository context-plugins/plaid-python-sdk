from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr


class ConsentedAccount(SdkBaseModel):
    """A financial institution account."""

    account_id: Optional[str] = UNSET
    """Plaid's unique identifier for the account. Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    mask: Optional[str] = UNSET
    """The last 2-4 alphanumeric characters of an account's official account number"""

    name: Optional[str] = UNSET
    """The name of the account, either assigned by the user or by the financial institution itself"""

    official_name: Optional[str] = UNSET
    """The official name of the account as given by the financial institution"""

    type_: Optional[AccountTypeOrStr] = Field(default=UNSET, alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: OptionalNullable[AccountSubtypeOrStr] = UNSET
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""


class ConsentedAccountDict(TypedDict):
    account_id: NotRequired[str]
    mask: NotRequired[str]
    name: NotRequired[str]
    official_name: NotRequired[str]
    type_: NotRequired[AccountTypeOrStr]
    subtype: NotRequired[AccountSubtypeOrStr | None]
