from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .security_override import SecurityOverride, SecurityOverrideDict


class InvestmentsTransactionsOverride(SdkBaseModel):
    """Specify the list of investments transactions on the account."""

    date: Date
    """Posting date for the transaction. Must be formatted as an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    date."""

    name: str
    """The institution's description of the transaction."""

    quantity: float
    """The number of units of the security involved in this transaction. Must be positive if the type is a buy and
    negative if the type is a sell."""

    price: float
    """The price of the security at which this transaction occurred."""

    fees: Optional[float] = UNSET
    """The combined value of all fees applied to this transaction."""

    type_: str = Field(alias="type")
    """The type of the investment transaction. Possible values are: ``buy``: Buying an investment ``sell``: Selling an
    investment ``cash``: Activity that modifies a cash position ``fee``: A fee on the account ``transfer``: Activity
    that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""

    currency: str
    """Either a valid ``iso_currency_code`` or ``unofficial_currency_code``"""

    security: Optional[SecurityOverride] = UNSET
    """Specify the security associated with the holding or investment transaction. When inputting custom security data
    to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the
    data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a
    security identifier (``ticker_symbol``, ``cusip``, or ``isin``) are required."""


class InvestmentsTransactionsOverrideDict(TypedDict):
    date: Date
    name: str
    quantity: float
    price: float
    fees: NotRequired[float]
    type_: str
    currency: str
    security: NotRequired[SecurityOverride | SecurityOverrideDict]
