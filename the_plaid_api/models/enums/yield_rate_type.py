from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class YieldRateType(str, Enum):
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

    COUPON = "coupon"
    COUPON_EQUIVALENT = "coupon_equivalent"
    DISCOUNT = "discount"
    YIELD = "yield"

    __str__ = str.__str__


YieldRateTypeOrStr: TypeAlias = Annotated[YieldRateType | str, open_enum_validator(YieldRateType)]
