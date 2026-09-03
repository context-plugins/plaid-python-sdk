from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .account_insights import AccountInsights, AccountInsightsDict
from .asset_report_account_balance import AssetReportAccountBalance, AssetReportAccountBalanceDict
from .asset_report_investments import AssetReportInvestments, AssetReportInvestmentsDict
from .asset_report_transaction import AssetReportTransaction, AssetReportTransactionDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.ownership_type import OwnershipTypeOrStr
from .enums.verification_status4 import VerificationStatus4OrStr
from .historical_balance import HistoricalBalance, HistoricalBalanceDict
from .owner import Owner, OwnerDict


class AccountAssets(SdkBaseModel):
    """Asset information about an account"""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    The ``account_id`` can also change if the ``access_token`` is deleted and the same credentials that were used to
    generate that ``access_token`` are used to generate a new ``access_token`` on a later date. In that case, the new
    ``account_id`` will be different from the old ``account_id``.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    balances: AssetReportAccountBalance
    """A set of fields describing the balance for an account. Balance information may be cached unless the balance
    object was returned by ``/accounts/balance/get``."""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    name: str
    """The name of the account, either assigned by the user or by the financial institution itself"""

    official_name: str | None
    """The official name of the account as given by the financial institution"""

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

    verification_status: Optional[VerificationStatus4OrStr] = UNSET
    """The current verification status of an Auth Item initiated through Automated or Manual micro-deposits. Returned
    for Auth Items only.

    ``pending_automatic_verification``: The Item is pending automatic verification.

    ``pending_manual_verification``: The Item is pending manual micro-deposit verification. Items remain in this state
    until the user successfully verifies the micro-deposit.

    ``automatically_verified``: The Item has successfully been automatically verified.

    ``manually_verified``: The Item has successfully been manually verified.

    ``verification_expired``: Plaid was unable to automatically verify the deposit within 7 calendar days and will no
    longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    ``verification_failed``: The Item failed manual micro-deposit verification because the user exhausted all 3
    verification attempts. Users may retry by submitting their information again through Link.

    ``database_matched``: (deprecated) The Item has successfully been verified using Plaid's data sources. Only returned
    for Auth Items created via Database Match."""

    persistent_account_id: Optional[str] = UNSET
    """A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account
    across different Items for depository accounts. This is currently an opt-in field and only supported for Chase
    Items."""

    days_available: float
    """The duration of transaction history available within this report for this Item, typically defined as the time
    since the date of the earliest transaction in that account."""

    transactions: list[AssetReportTransaction]
    """Transaction history associated with the account."""

    investments: Optional[AssetReportInvestments] = UNSET
    """A set of fields describing the investments data on an account."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners. For business accounts, the name
    reported may be either the name of the individual or the name of the business, depending on the institution.
    Multiple owners on a single account will be represented in the same ``owner`` object, not in multiple owner objects
    within the array. In API versions 2018-05-22 and earlier, the ``owners`` object is not returned, and instead
    identity information is returned in the top level ``identity`` object. For more details, see `Plaid API versioning
    <https://plaid.com/docs/api/versioning/#version-2019-05-29>`__"""

    ownership_type: OptionalNullable[OwnershipTypeOrStr] = UNSET
    """How an asset is owned.

    ``association``: Ownership by a corporation, partnership, or unincorporated association, including for-profit and
    not-for-profit organizations. ``individual``: Ownership by an individual. ``joint``: Joint ownership by multiple
    parties. ``trust``: Ownership by a revocable or irrevocable trust."""

    historical_balances: list[HistoricalBalance]
    """Calculated data about the historical balances on the account.

    Available for ``credit`` and ``depository`` type accounts."""

    account_insights: OptionalNullable[AccountInsights] = UNSET
    """This is a container object for all lending-related insights. This field will be returned only for European
    customers."""


class AccountAssetsDict(TypedDict):
    account_id: str
    balances: AssetReportAccountBalance | AssetReportAccountBalanceDict
    mask: str | None
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    verification_status: NotRequired[VerificationStatus4OrStr]
    persistent_account_id: NotRequired[str]
    days_available: float
    transactions: list[AssetReportTransaction | AssetReportTransactionDict]
    investments: NotRequired[AssetReportInvestments | AssetReportInvestmentsDict]
    owners: list[Owner | OwnerDict]
    ownership_type: NotRequired[OwnershipTypeOrStr | None]
    historical_balances: list[HistoricalBalance | HistoricalBalanceDict]
    account_insights: NotRequired[AccountInsights | AccountInsightsDict | None]
