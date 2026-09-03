from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .security_override import SecurityOverride, SecurityOverrideDict


class HoldingsOverride(SdkBaseModel):
    """Specify the holdings on the account."""

    institution_price: float
    """The last price given by the institution for this security"""

    institution_price_as_of: Optional[Date] = UNSET
    """The date at which ``institution_price`` was current. Must be formatted as an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ date."""

    cost_basis: Optional[float] = UNSET
    """The total cost basis of the holding (e.g., the total amount spent to acquire all assets currently in the
    holding)."""

    quantity: float
    """The total quantity of the asset held, as reported by the financial institution."""

    currency: str
    """Either a valid ``iso_currency_code`` or ``unofficial_currency_code``"""

    security: SecurityOverride
    """Specify the security associated with the holding or investment transaction. When inputting custom security data
    to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the
    data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a
    security identifier (``ticker_symbol``, ``cusip``, or ``isin``) are required."""


class HoldingsOverrideDict(TypedDict):
    institution_price: float
    institution_price_as_of: NotRequired[Date]
    cost_basis: NotRequired[float]
    quantity: float
    currency: str
    security: SecurityOverride | SecurityOverrideDict
