from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.transaction_type import TransactionTypeOrStr
from .payment_meta import PaymentMeta, PaymentMetaDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class TransactionBase(SdkBaseModel):
    """A representation of a transaction"""

    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: float
    """The settled value of the transaction, denominated in the transaction's currency, as stated in
    ``iso_currency_code`` or ``unofficial_currency_code``. For all products except Income: Positive values when money
    moves out of the account; negative values when money moves in. For example, debit card purchases are positive;
    credit card payments, direct deposits, and refunds are negative. For Income endpoints, values are positive when
    representing income."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the transaction. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the transaction. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    category: Optional[list[str | None]] = UNSET
    """A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget.

    All Transactions implementations are recommended to use the new ``personal_finance_category`` instead of
    ``category``, as it provides greater accuracy and more meaningful categorization.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    category_id: OptionalNullable[str] = UNSET
    """The ID of the category to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget.

    All Transactions implementations are recommended to use the new ``personal_finance_category`` instead of
    ``category``, as it provides greater accuracy and more meaningful categorization.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DD`` ). To receive information about the date that a posted transaction was initiated, see the
    ``authorized_date`` field."""

    location: Optional[TransactionLocation] = UNSET
    """A representation of where a transaction took place. Location data is provided only for transactions at physical
    locations, not for online transactions. Location data availability depends primarily on the merchant and is most
    likely to be populated for transactions at large retail chains; small, local businesses are less likely to have
    location data available."""

    name: Optional[str] = UNSET
    """The merchant name or transaction description.

    Note: While Plaid does not currently plan to remove this field, it is a legacy field that is not actively
    maintained. Use ``merchant_name`` instead for the merchant name.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/sync`` or
    ``/transactions/get``, this field will always appear. If the ``transactions`` object was returned by an Assets
    endpoint such as ``/asset_report/get`` or ``/asset_report/pdf/get``, this field will only appear in an Asset Report
    with Insights."""

    merchant_name: OptionalNullable[str] = UNSET
    """The merchant name, as enriched by Plaid from the ``name`` field. This is typically a more human-readable version
    of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers)
    where there is no meaningful merchant name, this value will be ``null``."""

    original_description: OptionalNullable[str] = UNSET
    """The string returned by the financial institution to describe the transaction. For transactions returned by
    ``/transactions/sync`` or ``/transactions/get``, this field will only be included if the client has set
    ``options.include_original_description`` to ``true``."""

    payment_meta: Optional[PaymentMeta] = UNSET
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all
    fields will be ``null``.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/sync`` or
    ``/transactions/get``, the ``payment_meta`` key will always appear, but no data elements are guaranteed. If the
    ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    pending: bool
    """When ``true``, identifies the transaction as pending or unsettled. Pending transaction details (name, type,
    amount, category ID) may change before they are settled. Not all institutions provide pending transactions."""

    pending_transaction_id: OptionalNullable[str] = UNSET
    """The ID of a posted transaction's associated pending transaction, where applicable. Not all institutions provide
    pending transactions."""

    account_owner: OptionalNullable[str] = UNSET
    """This field is not typically populated and only relevant when dealing with sub-accounts. A sub-account most
    commonly exists in cases where a single account is linked to multiple cards, each with its own card number and card
    holder name; each card will be considered a sub-account. If the account does have sub-accounts, this field will
    typically be some combination of the sub-account owner's name and/or the sub-account mask. The format of this field
    is not standardized and will vary based on institution."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    transaction_type: Optional[TransactionTypeOrStr] = UNSET
    """Please use the ``payment_channel`` field, ``transaction_type`` will be deprecated in the future.

    ``digital:`` transactions that took place online.

    ``place:`` transactions that were made at a physical location.

    ``special:`` transactions that relate to banks, e.g. fees or deposits.

    ``unresolved:`` transactions that do not fit into the other three types."""

    logo_url: OptionalNullable[str] = UNSET
    """The URL of a logo associated with this transaction, if available. The logo will always be a 100×100 pixel PNG
    file."""

    website: OptionalNullable[str] = UNSET
    """The website associated with this transaction, if available."""


class TransactionBaseDict(TypedDict):
    account_id: str
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    category: NotRequired[list[str | None]]
    category_id: NotRequired[str | None]
    check_number: NotRequired[str | None]
    date: Date
    location: NotRequired[TransactionLocation | TransactionLocationDict]
    name: NotRequired[str]
    merchant_name: NotRequired[str | None]
    original_description: NotRequired[str | None]
    payment_meta: NotRequired[PaymentMeta | PaymentMetaDict]
    pending: bool
    pending_transaction_id: NotRequired[str | None]
    account_owner: NotRequired[str | None]
    transaction_id: str
    transaction_type: NotRequired[TransactionTypeOrStr]
    logo_url: NotRequired[str | None]
    website: NotRequired[str | None]
