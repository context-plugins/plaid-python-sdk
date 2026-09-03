from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.yield_rate_type import YieldRateTypeOrStr


class YieldRate(SdkBaseModel):
    """Details about a fixed income security's expected rate of return."""

    percentage: float
    """The fixed income security's expected rate of return."""

    type_: YieldRateTypeOrStr | None = Field(alias="type")
    """The type of rate which indicates how the predicted yield was calculated. It is one of:

    ``coupon``: the annualized interest rate for securities with a one-year term or longer, such as treasury notes and
    bonds.

    ``coupon_equivalent``: the calculated equivalent for the annualized interest rate factoring in the discount rate and
    time to maturity, for shorter term, non-interest-bearing securities such as treasury bills.

    ``discount``: the rate at which the present value or cost is discounted from the future value upon maturity, also
    known as the face value.

    ``yield``: the total predicted rate of return factoring in both the discount rate and the coupon rate, applicable to
    securities such as exchange-traded bonds which can both be interest-bearing as well as sold at a discount off their
    face value."""


class YieldRateDict(TypedDict):
    percentage: float
    type_: YieldRateTypeOrStr | None
