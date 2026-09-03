from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.credit_pay_stub_pay_basis_type import CreditPayStubPayBasisTypeOrStr
from .pay_stub_distribution_breakdown import PayStubDistributionBreakdown, PayStubDistributionBreakdownDict


class PayStubPayPeriodDetails(SdkBaseModel):
    """Details about the pay period."""

    pay_amount: float | None
    """The amount of the paycheck."""

    distribution_breakdown: list[PayStubDistributionBreakdown]
    end_date: Date | None
    """The date on which the pay period ended, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    gross_earnings: float | None
    """Total earnings before tax/deductions."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the net pay. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    pay_date: Date | None
    """The date on which the pay stub was issued, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    pay_frequency: str | None
    """The frequency at which an individual is paid."""

    pay_basis: Optional[CreditPayStubPayBasisTypeOrStr] = UNSET
    """The explicit pay basis on the paystub (if present)."""

    start_date: Date | None
    """The date on which the pay period started, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the net pay. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""


class PayStubPayPeriodDetailsDict(TypedDict):
    pay_amount: float | None
    distribution_breakdown: list[PayStubDistributionBreakdown | PayStubDistributionBreakdownDict]
    end_date: Date | None
    gross_earnings: float | None
    iso_currency_code: str | None
    pay_date: Date | None
    pay_frequency: str | None
    pay_basis: NotRequired[CreditPayStubPayBasisTypeOrStr]
    start_date: Date | None
    unofficial_currency_code: str | None
