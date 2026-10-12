from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .holding_tax_lot import HoldingTaxLot, HoldingTaxLotDict


class Holding(SdkBaseModel):
    """A securities holding at an institution."""

    account_id: str
    """The Plaid ``account_id`` associated with the holding."""

    security_id: str
    """The Plaid ``security_id`` associated with the holding. Security data is not specific to a user's account; any
    user who held the same security at the same financial institution at the same time would have identical security
    data. The ``security_id`` for the same security will typically be the same across different institutions, but this
    is not guaranteed. The ``security_id`` does not typically change, but may change if inherent details of the security
    change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change."""

    institution_price: float
    """The last price given by the institution for this security."""

    institution_price_as_of: OptionalNullable[Date] = UNSET
    """The date at which ``institution_price`` was current."""

    institution_price_datetime: OptionalNullable[RFC3339DateTime] = UNSET
    """Date and time at which ``institution_price`` was current, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).

    This field is returned for select financial institutions and comes as provided by the institution. It may contain
    default time values (such as 00:00:00)."""

    institution_value: float
    """The value of the holding, as reported by the institution."""

    cost_basis: float | None
    """The total cost basis of the holding (e.g., the total amount spent to acquire all assets currently in the
    holding)."""

    quantity: float
    """The total quantity of the asset held, as reported by the financial institution. If the security is an option,
    ``quantity`` will reflect the total number of options (typically the number of contracts multiplied by 100), not the
    number of contracts."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the holding. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the holding. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    vested_quantity: OptionalNullable[float] = UNSET
    """The total quantity of vested assets held, as reported by the financial institution. Vested assets are only
    associated with `equities
    <https://plaid.com/docs/api/products/investments/#investments-holdings-get-response-securities-type>`__."""

    vested_value: OptionalNullable[float] = UNSET
    """The value of the vested holdings as reported by the institution."""

    tax_lots: Optional[list[HoldingTaxLot]] = UNSET
    """Per-lot acquisition data for this holding. An empty array indicates the institution does not provide lot-level
    data."""


class HoldingDict(TypedDict):
    account_id: str
    security_id: str
    institution_price: float
    institution_price_as_of: NotRequired[Date | None]
    institution_price_datetime: NotRequired[RFC3339DateTime | None]
    institution_value: float
    cost_basis: float | None
    quantity: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    vested_quantity: NotRequired[float | None]
    vested_value: NotRequired[float | None]
    tax_lots: NotRequired[list[HoldingTaxLotDict]]
