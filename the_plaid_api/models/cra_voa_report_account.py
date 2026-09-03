from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .base_report_investments import BaseReportInvestments, BaseReportInvestmentsDict
from .consumer_dispute import ConsumerDispute, ConsumerDisputeDict
from .cra_voa_report_account_balances import CraVoaReportAccountBalances, CraVoaReportAccountBalancesDict
from .cra_voa_report_transactions_insights import CraVoaReportTransactionsInsights, CraVoaReportTransactionsInsightsDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.ownership_type import OwnershipTypeOrStr
from .owner import Owner, OwnerDict


class CraVoaReportAccount(SdkBaseModel):
    """VOA Report information about an account."""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    balances: CraVoaReportAccountBalances
    """VOA Report information about an account's balances."""

    consumer_disputes: list[ConsumerDispute]
    """The information about previously submitted valid dispute statements by the consumer"""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

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

    days_available: float
    """The duration of transaction history available within this report for this Item, typically defined as the time
    since the date of the earliest transaction in that account."""

    transactions_insights: CraVoaReportTransactionsInsights
    """Transaction data associated with the account."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners."""

    ownership_type: OwnershipTypeOrStr | None
    """How an asset is owned.

    ``association``: Ownership by a corporation, partnership, or unincorporated association, including for-profit and
    not-for-profit organizations. ``individual``: Ownership by an individual. ``joint``: Joint ownership by multiple
    parties. ``trust``: Ownership by a revocable or irrevocable trust."""

    investments: OptionalNullable[BaseReportInvestments] = UNSET
    """A set of fields describing the investments data on an account."""


class CraVoaReportAccountDict(TypedDict):
    account_id: str
    balances: CraVoaReportAccountBalances | CraVoaReportAccountBalancesDict
    consumer_disputes: list[ConsumerDispute | ConsumerDisputeDict]
    mask: str | None
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    days_available: float
    transactions_insights: CraVoaReportTransactionsInsights | CraVoaReportTransactionsInsightsDict
    owners: list[Owner | OwnerDict]
    ownership_type: OwnershipTypeOrStr | None
    investments: NotRequired[BaseReportInvestments | BaseReportInvestmentsDict | None]
