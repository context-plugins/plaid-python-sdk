from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .credit_category import CreditCategory, CreditCategoryDict
from .enums.base_report_transaction_type import BaseReportTransactionTypeOrStr
from .personal_finance_category import PersonalFinanceCategory, PersonalFinanceCategoryDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class BaseReportTransaction(SdkBaseModel):
    """A transaction on the Base Report"""

    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: float
    """The settled value of the transaction, denominated in the transaction's currency, as stated in
    ``iso_currency_code`` or ``unofficial_currency_code``. Positive values when money moves out of the account; negative
    values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits,
    and refunds are negative."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the transaction. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the transaction. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    name: OptionalNullable[str] = UNSET
    """The merchant name or transaction description.

    Note: This is a legacy field that is not actively maintained. Use ``merchant_name`` instead for the merchant
    name."""

    original_description: str | None
    """The string returned by the financial institution to describe the transaction."""

    credit_category: OptionalNullable[CreditCategory] = UNSET
    """Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such
    use cases.

    See the https://plaid.com/documents/credit-category-taxonomy.csv for a full list of credit categories."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DD`` )."""

    date_transacted: OptionalNullable[str] = UNSET
    """The date on which the transaction took place, in ISO 8601 format."""

    location: Optional[TransactionLocation] = UNSET
    """A representation of where a transaction took place. Location data is provided only for transactions at physical
    locations, not for online transactions. Location data availability depends primarily on the merchant and is most
    likely to be populated for transactions at large retail chains; small, local businesses are less likely to have
    location data available."""

    merchant_name: OptionalNullable[str] = UNSET
    """The merchant name, as enriched by Plaid from the ``name`` field. This is typically a more human-readable version
    of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers)
    where there is no meaningful merchant name, this value will be ``null``."""

    pending: bool
    """When ``true``, identifies the transaction as pending or unsettled. Pending transaction details (name, type,
    amount, category ID) may change before they are settled."""

    account_owner: OptionalNullable[str] = UNSET
    """The name of the account owner. This field is not typically populated and only relevant when dealing with
    sub-accounts."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    transaction_type: OptionalNullable[BaseReportTransactionTypeOrStr] = UNSET
    """``digital:`` transactions that took place online.

    ``place:`` transactions that were made at a physical location.

    ``special:`` transactions that relate to banks, e.g. fees or deposits.

    ``unresolved:`` transactions that do not fit into the other types."""

    category: Optional[list[str | None]] = UNSET
    """A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget."""

    category_id: OptionalNullable[str] = UNSET
    """The ID of the category to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget."""

    personal_finance_category: OptionalNullable[PersonalFinanceCategory] = UNSET


class BaseReportTransactionDict(TypedDict):
    account_id: str
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    name: NotRequired[str | None]
    original_description: str | None
    credit_category: NotRequired[CreditCategory | CreditCategoryDict | None]
    check_number: NotRequired[str | None]
    date: Date
    date_transacted: NotRequired[str | None]
    location: NotRequired[TransactionLocation | TransactionLocationDict]
    merchant_name: NotRequired[str | None]
    pending: bool
    account_owner: NotRequired[str | None]
    transaction_id: str
    transaction_type: NotRequired[BaseReportTransactionTypeOrStr | None]
    category: NotRequired[list[str | None]]
    category_id: NotRequired[str | None]
    personal_finance_category: NotRequired[PersonalFinanceCategory | PersonalFinanceCategoryDict | None]
