from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .client_provided_transaction_location import (
    ClientProvidedTransactionLocation,
    ClientProvidedTransactionLocationDict,
)
from .enums.enrich_transaction_direction import EnrichTransactionDirectionOrStr


class ClientProvidedTransaction(SdkBaseModel):
    """A client-provided transaction for Plaid to enrich."""

    id: str
    """A unique ID for the transaction used to help you tie data back to your systems."""

    user_id: Optional[str] = UNSET
    """The Plaid generated ID that identifies the end user for whom you would like to enrich transactions."""

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
    """The raw description of the transaction. If you have location data in available an unstructured format, it may be
    appended to the ``description`` field."""

    amount: float
    """The absolute value of the transaction (>= 0). When testing Enrich, note that ``amount`` data should be realistic.
    Unrealistic or inaccurate ``amount`` data may result in reduced quality output."""

    direction: EnrichTransactionDirectionOrStr
    """The direction of the transaction from the perspective of the account holder:

    ``OUTFLOW`` - Includes outgoing transfers, purchases, and fees. (Typically represented as a negative value on
    checking accounts and debit cards and a positive value on credit cards.)

    ``INFLOW`` - Includes incoming transfers, refunds, and income. (Typically represented as a positive value on
    checking accounts and debit cards and a negative value on credit cards.)"""

    iso_currency_code: str
    """The ISO-4217 currency code of the transaction e.g. USD."""

    location: Optional[ClientProvidedTransactionLocation] = UNSET
    """A representation of where a transaction took place.

    Use this field to pass in structured location information you may have about your transactions. Providing location
    data is optional but can increase result quality. If you have unstructured location information, it may be appended
    to the ``description`` field."""

    mcc: Optional[str] = UNSET
    """Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities."""

    date_posted: Optional[Date] = UNSET
    """The date the transaction posted, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format."""


class ClientProvidedTransactionDict(TypedDict):
    id: str
    user_id: NotRequired[str]
    client_user_id: NotRequired[str]
    client_account_id: NotRequired[str]
    account_type: NotRequired[str]
    account_subtype: NotRequired[str]
    description: str
    amount: float
    direction: EnrichTransactionDirectionOrStr
    iso_currency_code: str
    location: NotRequired[ClientProvidedTransactionLocation | ClientProvidedTransactionLocationDict]
    mcc: NotRequired[str]
    date_posted: NotRequired[Date]
