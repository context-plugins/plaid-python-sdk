from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_employment_refresh_report_transaction import (
    CraEmploymentRefreshReportTransaction,
    CraEmploymentRefreshReportTransactionDict,
)
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr


class CraEmploymentRefreshReportAccount(SdkBaseModel):
    """Employment Refresh Report information about an account."""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    name: str
    """The name of the account, either assigned by the user or by the financial institution itself."""

    official_name: str | None
    """The official name of the account as given by the financial institution."""

    type_: AccountTypeOrStr = Field(alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: AccountSubtypeOrStr | None
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    transactions: list[CraEmploymentRefreshReportTransaction]
    """Transaction history associated with the account for the Employment Refresh Report. Note that this transaction
    differs from a Base Report transaction in that it will only be deposits, and the amounts will be omitted."""


class CraEmploymentRefreshReportAccountDict(TypedDict):
    account_id: str
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    transactions: list[CraEmploymentRefreshReportTransactionDict]
