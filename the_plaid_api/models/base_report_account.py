from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base_report_account_balances import BaseReportAccountBalances, BaseReportAccountBalancesDict
from .base_report_account_insights import BaseReportAccountInsights, BaseReportAccountInsightsDict
from .base_report_account_metadata import BaseReportAccountMetadata, BaseReportAccountMetadataDict
from .base_report_attributes import BaseReportAttributes, BaseReportAttributesDict
from .base_report_historical_balance import BaseReportHistoricalBalance, BaseReportHistoricalBalanceDict
from .base_report_transaction import BaseReportTransaction, BaseReportTransactionDict
from .consumer_dispute import ConsumerDispute, ConsumerDisputeDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.ownership_type import OwnershipTypeOrStr
from .owner import Owner, OwnerDict


class BaseReportAccount(SdkBaseModel):
    """Base Report information about an account"""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    balances: BaseReportAccountBalances
    """Information about an account's balances."""

    consumer_disputes: list[ConsumerDispute]
    """The information about previously submitted valid dispute statements by the consumer"""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    metadata: BaseReportAccountMetadata
    """Metadata about the extracted account."""

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

    days_available: float
    """The duration of transaction history available within this report for this Item, typically defined as the time
    since the date of the earliest transaction in that account."""

    transactions: list[BaseReportTransaction]
    """Transaction history associated with the account. Transaction history returned by endpoints such as
    ``/transactions/get`` or ``/investments/transactions/get`` will be returned in the top-level ``transactions`` field
    instead. Some transactions may have their details masked in accordance to the FCRA. These will appear with a
    ``credit_category`` of ``MASKED_TRANSACTION_CATEGORY``."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners. For business accounts, the name
    reported may be either the name of the individual or the name of the business, depending on the institution.
    Multiple owners on a single account will be represented in the same ``owner`` object, not in multiple owner objects
    within the array. This array can also be empty if no owners are found."""

    ownership_type: OwnershipTypeOrStr | None
    """How an asset is owned.

    ``association``: Ownership by a corporation, partnership, or unincorporated association, including for-profit and
    not-for-profit organizations. ``individual``: Ownership by an individual. ``joint``: Joint ownership by multiple
    parties. ``trust``: Ownership by a revocable or irrevocable trust."""

    historical_balances: Optional[list[BaseReportHistoricalBalance]] = UNSET
    """Calculated data about the historical balances on the account. Currently not supported by ``brokerage`` or
    ``investment`` accounts."""

    account_insights: Optional[BaseReportAccountInsights] = UNSET
    """Calculated insights derived from transaction-level data. This field has been deprecated in favor of `Base Report
    attributes aggregated across accounts
    <https://plaid.com/docs/api/products/check/#cra-check_report-base_report-get-response-report-attributes>`__ and will
    be removed in a future release."""

    attributes: Optional[BaseReportAttributes] = UNSET
    """Calculated attributes derived from transaction-level data."""


class BaseReportAccountDict(TypedDict):
    account_id: str
    balances: BaseReportAccountBalancesDict
    consumer_disputes: list[ConsumerDisputeDict]
    mask: str | None
    metadata: BaseReportAccountMetadataDict
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    days_available: float
    transactions: list[BaseReportTransactionDict]
    owners: list[OwnerDict]
    ownership_type: OwnershipTypeOrStr | None
    historical_balances: NotRequired[list[BaseReportHistoricalBalanceDict]]
    account_insights: NotRequired[BaseReportAccountInsightsDict]
    attributes: NotRequired[BaseReportAttributesDict]
