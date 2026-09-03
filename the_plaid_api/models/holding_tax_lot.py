from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.holding_tax_lot_position_type import HoldingTaxLotPositionTypeOrStr


class HoldingTaxLot(SdkBaseModel):
    """A single acquisition lot within a holding."""

    institution_lot_id: str | None
    """The financial institution's identifier for this lot. Null if the institution does not provide a lot
    identifier."""

    original_purchase_datetime: RFC3339DateTime | None
    """The date and time this lot was acquired, in ISO 8601 format. Null if the institution does not provide acquisition
    datetime data."""

    quantity: float | None
    """The number of units of the security in this lot."""

    purchase_price: float | None
    """The price per unit of the security at the time this lot was acquired."""

    cost_basis: float | None
    """The total cost basis of this lot, inclusive of any fees."""

    current_value: float | None
    """The current market value of this lot."""

    position_type: HoldingTaxLotPositionTypeOrStr | None
    """Indicates whether a holding lot position is long or short. Possible values are ``LONG`` and ``SHORT``."""


class HoldingTaxLotDict(TypedDict):
    institution_lot_id: str | None
    original_purchase_datetime: RFC3339DateTime | None
    quantity: float | None
    purchase_price: float | None
    cost_basis: float | None
    current_value: float | None
    position_type: HoldingTaxLotPositionTypeOrStr | None
