from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MortgageInterestRate(SdkBaseModel):
    """Object containing metadata about the interest rate for the mortgage."""

    percentage: float | None
    """Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan."""

    type_: str | None = Field(alias="type")
    """The type of interest charged (fixed or variable)."""


class MortgageInterestRateDict(TypedDict):
    percentage: float | None
    type_: str | None
