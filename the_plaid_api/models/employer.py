from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .address_data_nullable import AddressDataNullable, AddressDataNullableDict


class Employer(SdkBaseModel):
    """Data about the employer."""

    employer_id: str
    """Plaid's unique identifier for the employer."""

    name: str
    """The name of the employer"""

    address: AddressDataNullable | None
    """Data about the components comprising an address."""

    confidence_score: float
    """A number from 0 to 1 indicating Plaid's level of confidence in the pairing between the employer and the
    institution (not yet implemented)."""


class EmployerDict(TypedDict):
    employer_id: str
    name: str
    address: AddressDataNullable | AddressDataNullableDict | None
    confidence_score: float
