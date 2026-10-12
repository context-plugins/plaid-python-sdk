from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .counterparty import Counterparty, CounterpartyDict
from .enums.transaction_payment_channel import TransactionPaymentChannelOrStr
from .personal_finance_category import PersonalFinanceCategory, PersonalFinanceCategoryDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class Enrichments(SdkBaseModel):
    """A grouping of the Plaid produced transaction enrichment fields."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    counterparties: list[Counterparty]
    """The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution,
    are extracted by Plaid from the raw description."""

    entity_id: OptionalNullable[str] = UNSET
    """A unique, stable, Plaid-generated ID that maps to the primary counterparty."""

    legacy_category_id: OptionalNullable[str] = UNSET
    """The ID of the legacy category to which this transaction belongs. For a full list of legacy categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget.

    We recommend using the ``personal_finance_category`` for transaction categorization to obtain the best results."""

    legacy_category: OptionalNullable[list[str]] = UNSET
    """A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy
    categories, see https://plaid.com/docs/api/products/transactions/#categoriesget.

    We recommend using the ``personal_finance_category`` for transaction categorization to obtain the best results."""

    location: TransactionLocation
    """A representation of where a transaction took place. Location data is provided only for transactions at physical
    locations, not for online transactions. Location data availability depends primarily on the merchant and is most
    likely to be populated for transactions at large retail chains; small, local businesses are less likely to have
    location data available."""

    logo_url: str | None
    """The URL of a logo associated with this transaction, if available. The logo will always be a 100×100 pixel PNG
    file."""

    merchant_name: str | None
    """The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid
    from the raw description."""

    payment_channel: TransactionPaymentChannelOrStr
    """The channel used to make a payment. ``online:`` transactions that took place online.

    ``in store:`` transactions that were made at a physical location.

    ``other:`` transactions that relate to banks, e.g. fees or deposits."""

    phone_number: str | None
    """The phone number associated with the counterparty in E.164 format. If there is a location match (i.e. a street
    address is returned in the location object), the phone number will be location specific."""

    personal_finance_category: PersonalFinanceCategory | None
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not
    limited to such use cases.

    See the `taxonomy CSV file <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance
    categories. If you are migrating to personal finance categories from the legacy categories, also refer to the
    `migration guide <https://plaid.com/docs/transactions/pfc-migration/>`__."""

    personal_finance_category_icon_url: str
    """The URL of an icon associated with the primary personal finance category. The icon will always be a 100×100 pixel
    PNG file."""

    website: str | None
    """The website associated with this transaction."""


class EnrichmentsDict(TypedDict):
    check_number: NotRequired[str | None]
    counterparties: list[CounterpartyDict]
    entity_id: NotRequired[str | None]
    legacy_category_id: NotRequired[str | None]
    legacy_category: NotRequired[list[str] | None]
    location: TransactionLocationDict
    logo_url: str | None
    merchant_name: str | None
    payment_channel: TransactionPaymentChannelOrStr
    phone_number: str | None
    personal_finance_category: PersonalFinanceCategoryDict | None
    personal_finance_category_icon_url: str
    website: str | None
