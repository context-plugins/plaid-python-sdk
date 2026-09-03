from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .client_customization import ClientCustomization, ClientCustomizationDict
from .enrichments import Enrichments, EnrichmentsDict
from .enums.enrich_transaction_direction import EnrichTransactionDirectionOrStr


class ClientProvidedEnrichedTransaction(SdkBaseModel):
    """A client-provided transaction that Plaid has enriched."""

    id: str
    """The unique ID for the transaction as provided by you in the request."""

    client_user_id: Optional[str] = UNSET
    """A unique user id used to group transactions for a given user, as a unique identifier from your application.
    Personally identifiable information, such as an email address or phone number, should not be used in the
    ``client_user_id``."""

    client_account_id: Optional[str] = UNSET
    """A unique account id used to group transactions for a given account, as a unique identifier from your application.
    Personally identifiable information, such as an email address or phone number, should not be used in the
    ``client_account_id``."""

    account_type: Optional[str] = UNSET
    """The account type associated with the transaction. For a full list of valid types and subtypes, see the `Account
    schema <https://plaid.com/docs/api/accounts#account-type-schema>`__."""

    account_subtype: Optional[str] = UNSET
    """The account subtype associated with the transaction. For a full list of valid types and subtypes, see the
    `Account schema <https://plaid.com/docs/api/accounts#account-type-schema>`__."""

    description: str
    """The raw description of the transaction."""

    amount: float
    """The absolute value of the transaction (>= 0)"""

    direction: Optional[EnrichTransactionDirectionOrStr] = UNSET
    """The direction of the transaction from the perspective of the account holder:

    ``OUTFLOW`` - Includes outgoing transfers, purchases, and fees. (Typically represented as a negative value on
    checking accounts and debit cards and a positive value on credit cards.)

    ``INFLOW`` - Includes incoming transfers, refunds, and income. (Typically represented as a positive value on
    checking accounts and debit cards and a negative value on credit cards.)"""

    iso_currency_code: str
    """The ISO-4217 currency code of the transaction e.g. USD."""

    enrichments: Enrichments
    """A grouping of the Plaid produced transaction enrichment fields."""

    client_customization: OptionalNullable[ClientCustomization] = UNSET
    """Custom client fields"""


class ClientProvidedEnrichedTransactionDict(TypedDict):
    id: str
    client_user_id: NotRequired[str]
    client_account_id: NotRequired[str]
    account_type: NotRequired[str]
    account_subtype: NotRequired[str]
    description: str
    amount: float
    direction: NotRequired[EnrichTransactionDirectionOrStr]
    iso_currency_code: str
    enrichments: Enrichments | EnrichmentsDict
    client_customization: NotRequired[ClientCustomization | ClientCustomizationDict | None]
