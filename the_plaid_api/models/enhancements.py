from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .counterparty import Counterparty, CounterpartyDict
from .enums.transaction_payment_channel import TransactionPaymentChannelOrStr
from .personal_finance_category import PersonalFinanceCategory, PersonalFinanceCategoryDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class Enhancements(SdkBaseModel):
    """A grouping of the Plaid produced transaction enhancement fields."""

    merchant_name: OptionalNullable[str] = UNSET
    """The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid
    from the raw description."""

    website: OptionalNullable[str] = UNSET
    """The website associated with this transaction, if available."""

    logo_url: OptionalNullable[str] = UNSET
    """The URL of a logo associated with this transaction, if available. The logo will always be a 100×100 pixel PNG
    file."""

    check_number: OptionalNullable[str] = UNSET
    """The check number of the transaction. This field is only populated for check transactions."""

    payment_channel: TransactionPaymentChannelOrStr
    """The channel used to make a payment. ``online:`` transactions that took place online.

    ``in store:`` transactions that were made at a physical location.

    ``other:`` transactions that relate to banks, e.g. fees or deposits."""

    category_id: str | None
    """The ID of the category to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget."""

    category: list[str]
    """A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget."""

    location: TransactionLocation
    """A representation of where a transaction took place. Location data is provided only for transactions at physical
    locations, not for online transactions. Location data availability depends primarily on the merchant and is most
    likely to be populated for transactions at large retail chains; small, local businesses are less likely to have
    location data available."""

    personal_finance_category: OptionalNullable[PersonalFinanceCategory] = UNSET
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not
    limited to such use cases.

    See the `taxonomy CSV file <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance
    categories. If you are migrating to personal finance categories from the legacy categories, also refer to the
    `migration guide <https://plaid.com/docs/transactions/pfc-migration/>`__."""

    personal_finance_category_icon_url: Optional[str] = UNSET
    """The URL of an icon associated with the primary personal finance category. The icon will always be a 100×100 pixel
    PNG file."""

    counterparties: Optional[list[Counterparty]] = UNSET
    """The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution,
    are extracted by Plaid from the raw description."""


class EnhancementsDict(TypedDict):
    merchant_name: NotRequired[str | None]
    website: NotRequired[str | None]
    logo_url: NotRequired[str | None]
    check_number: NotRequired[str | None]
    payment_channel: TransactionPaymentChannelOrStr
    category_id: str | None
    category: list[str]
    location: TransactionLocationDict
    personal_finance_category: NotRequired[PersonalFinanceCategoryDict | None]
    personal_finance_category_icon_url: NotRequired[str]
    counterparties: NotRequired[list[CounterpartyDict]]
