from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .business_finance_category import BusinessFinanceCategory, BusinessFinanceCategoryDict
from .client_customization import ClientCustomization, ClientCustomizationDict
from .enums.payment_channel import PaymentChannelOrStr
from .enums.transaction_code import TransactionCodeOrStr
from .enums.transaction_type import TransactionTypeOrStr
from .payment_meta import PaymentMeta, PaymentMetaDict
from .personal_finance_category import PersonalFinanceCategory, PersonalFinanceCategoryDict
from .transaction_counterparty import TransactionCounterparty, TransactionCounterpartyDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class Transaction(SdkBaseModel):
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

    category: OptionalNullable[list[str]] = UNSET
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

    location: TransactionLocation
    """A representation of where a transaction took place. Location data is provided only for transactions at physical
    locations, not for online transactions. Location data availability depends primarily on the merchant and is most
    likely to be populated for transactions at large retail chains; small, local businesses are less likely to have
    location data available."""

    name: str
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

    payment_meta: PaymentMeta
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all
    fields will be ``null``.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/sync`` or
    ``/transactions/get``, the ``payment_meta`` key will always appear, but no data elements are guaranteed. If the
    ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    pending: bool
    """When ``true``, identifies the transaction as pending or unsettled. Pending transaction details (name, type,
    amount, category ID) may change before they are settled. Not all institutions provide pending transactions."""

    pending_transaction_id: str | None
    """The ID of a posted transaction's associated pending transaction, where applicable. Not all institutions provide
    pending transactions."""

    account_owner: str | None
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

    authorized_date: Date | None
    """The date that the transaction was authorized. For posted transactions, the ``date`` field will indicate the
    posted date, but ``authorized_date`` will indicate the day the transaction was authorized by the financial
    institution. If presenting transactions to the user in a UI, the ``authorized_date``, when available, is generally
    preferable to use over the ``date`` field for posted transactions, as it will generally represent the date the user
    actually made the transaction. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DD`` )."""

    authorized_datetime: RFC3339DateTime | None
    """Date and time when a transaction was authorized in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` ). For posted transactions, the ``datetime`` field will indicate the posted date, but
    ``authorized_datetime`` will indicate the day the transaction was authorized by the financial institution. If
    presenting transactions to the user in a UI, the ``authorized_datetime``, when available, is generally preferable to
    use over the ``datetime`` field for posted transactions, as it will generally represent the date the user actually
    made the transaction.

    This field is returned for select financial institutions and comes as provided by the institution. It may contain
    default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later."""

    datetime: RFC3339DateTime | None
    """Date and time when a transaction was posted in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` ). For the date that the transaction was initiated, rather than posted, see the
    ``authorized_datetime`` field.

    This field is returned for select financial institutions and comes as provided by the institution. It may contain
    default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later."""

    payment_channel: PaymentChannelOrStr
    """The channel used to make a payment. ``online:`` transactions that took place online.

    ``in store:`` transactions that were made at a physical location.

    ``other:`` transactions that relate to banks, e.g. fees or deposits.

    This field replaces the ``transaction_type`` field."""

    personal_finance_category: OptionalNullable[PersonalFinanceCategory] = UNSET
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not
    limited to such use cases.

    See the `taxonomy CSV file <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance
    categories. If you are migrating to personal finance categories from the legacy categories, also refer to the
    `migration guide <https://plaid.com/docs/transactions/pfc-migration/>`__."""

    business_finance_category: OptionalNullable[BusinessFinanceCategory] = UNSET
    """Information describing the intent of the transaction. Most relevant for business finance use cases, but not
    limited to such use cases."""

    transaction_code: TransactionCodeOrStr | None
    """An identifier classifying the transaction type.

    This field is populated for European institutions, as well as certain institutions in the United States. For
    institutions where this classification is not available, this field is set to ``null``.

    ``adjustment:`` Bank adjustment

    ``atm:`` Cash deposit or withdrawal via an automated teller machine

    ``bank charge:`` Charge or fee levied by the institution

    ``bill payment``: Payment of a bill

    ``cash:`` Cash deposit or withdrawal

    ``cash advance:`` Cash advance drawn against a credit card or line of credit

    ``cashback:`` Cash withdrawal while making a debit card purchase

    ``cheque:`` Document ordering the payment of money to another person or organization

    ``direct debit:`` Automatic withdrawal of funds initiated by a third party at a regular interval

    ``interest:`` Interest earned or incurred

    ``late fee:`` Fee associated with a late or past-due payment

    ``membership fee:`` Annual or recurring membership fee

    ``payment:`` One-off outbound payment not classified as a bill payment, direct debit, or standing order

    ``purchase:`` Purchase made with a debit or credit card

    ``refund:`` Merchant credit or return, such as a refund of a prior purchase

    ``returned item fee:`` Fee for a returned item, such as a returned check or stop payment

    ``standing order:`` Payment instructed by the account holder to a third party at a regular interval

    ``transfer:`` Transfer of money between accounts"""

    personal_finance_category_icon_url: Optional[str] = UNSET
    """The URL of an icon associated with the primary personal finance category. The icon will always be a 100×100 pixel
    PNG file."""

    counterparties: Optional[list[TransactionCounterparty]] = UNSET
    """The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution,
    are extracted by Plaid from the raw description."""

    merchant_entity_id: OptionalNullable[str] = UNSET
    """A unique, stable, Plaid-generated ID that maps to the merchant. In the case of a merchant with multiple retail
    locations, this field will map to the broader merchant, not a specific location or store."""

    client_customization: OptionalNullable[ClientCustomization] = UNSET
    """Custom client fields"""


class TransactionDict(TypedDict):
    account_id: str
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    category: NotRequired[list[str] | None]
    category_id: NotRequired[str | None]
    check_number: NotRequired[str | None]
    date: Date
    location: TransactionLocationDict
    name: str
    merchant_name: NotRequired[str | None]
    original_description: NotRequired[str | None]
    payment_meta: PaymentMetaDict
    pending: bool
    pending_transaction_id: str | None
    account_owner: str | None
    transaction_id: str
    transaction_type: NotRequired[TransactionTypeOrStr]
    logo_url: NotRequired[str | None]
    website: NotRequired[str | None]
    authorized_date: Date | None
    authorized_datetime: RFC3339DateTime | None
    datetime: RFC3339DateTime | None
    payment_channel: PaymentChannelOrStr
    personal_finance_category: NotRequired[PersonalFinanceCategoryDict | None]
    business_finance_category: NotRequired[BusinessFinanceCategoryDict | None]
    transaction_code: TransactionCodeOrStr | None
    personal_finance_category_icon_url: NotRequired[str]
    counterparties: NotRequired[list[TransactionCounterpartyDict]]
    merchant_entity_id: NotRequired[str | None]
    client_customization: NotRequired[ClientCustomizationDict | None]
