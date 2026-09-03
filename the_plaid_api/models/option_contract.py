from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class OptionContract(SdkBaseModel):
    """Details about the option security.

    For the Sandbox environment, this data is currently only available if the Item is using a `custom Sandbox user
    <https://plaid.com/docs/sandbox/user-custom/>`__ and the ``ticker`` field of the custom security follows the `OCC
    Option Symbol <https://en.wikipedia.org/wiki/Option_symbol#The_OCC_Option_Symbol>`__ standard with no spaces. For an
    example of simulating this in Sandbox, see the `custom Sandbox GitHub
    <https://github.com/plaid/sandbox-custom-users>`__."""

    contract_type: str
    """The type of this option contract. It is one of:

    ``put``: for Put option contracts

    ``call``: for Call option contracts"""

    expiration_date: Date
    """The expiration date for this option contract, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    strike_price: float
    """The strike price for this option contract, per share of security."""

    underlying_security_ticker: str
    """The ticker of the underlying security for this option contract."""


class OptionContractDict(TypedDict):
    contract_type: str
    expiration_date: Date
    strike_price: float
    underlying_security_ticker: str
