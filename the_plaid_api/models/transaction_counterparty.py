from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .counterparty_numbers import CounterpartyNumbers, CounterpartyNumbersDict
from .enums.counterparty_type import CounterpartyTypeOrStr


class TransactionCounterparty(SdkBaseModel):
    """The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw
    description."""

    name: str
    """The name of the counterparty, such as the merchant or the financial institution, as extracted by Plaid from the
    raw description."""

    entity_id: OptionalNullable[str] = UNSET
    """A unique, stable, Plaid-generated ID that maps to the counterparty."""

    type_: CounterpartyTypeOrStr = Field(alias="type")
    """The counterparty type.

    ``merchant``: a provider of goods or services for purchase ``financial_institution``: a financial entity (bank,
    credit union, BNPL, fintech) ``payment_app``: a transfer or P2P app (e.g. Zelle) ``marketplace``: a marketplace
    (e.g. DoorDash, Google Play Store) ``payment_terminal``: a point-of-sale payment terminal (e.g. Square, Toast)
    ``income_source``: the payer in an income transaction (e.g., an employer, client, or government agency)"""

    website: str | None
    """The website associated with the counterparty."""

    logo_url: str | None
    """The URL of a logo associated with the counterparty, if available. The logo will always be a 100×100 pixel PNG
    file."""

    confidence_level: OptionalNullable[str] = UNSET
    """A description of how confident we are that the provided counterparty is involved in the transaction.

    ``VERY_HIGH``: We recognize this counterparty and we are more than 98% confident that it is involved in this
    transaction. ``HIGH``: We recognize this counterparty and we are more than 90% confident that it is involved in this
    transaction. ``MEDIUM``: We are moderately confident that this counterparty was involved in this transaction, but
    some details may differ from our records. ``LOW``: We didn't find a matching counterparty in our records, so we are
    returning a cleansed name parsed out of the request description. ``UNKNOWN``: We don't know the confidence level for
    this counterparty."""

    account_numbers: OptionalNullable[CounterpartyNumbers] = UNSET
    """Account numbers associated with the counterparty, when available. This field is currently only filled in for
    select financial institutions in Europe."""


class TransactionCounterpartyDict(TypedDict):
    name: str
    entity_id: NotRequired[str | None]
    type_: CounterpartyTypeOrStr
    website: str | None
    logo_url: str | None
    confidence_level: NotRequired[str | None]
    account_numbers: NotRequired[CounterpartyNumbers | CounterpartyNumbersDict | None]
