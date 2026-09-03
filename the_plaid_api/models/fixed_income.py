from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .yield_rate import YieldRate, YieldRateDict


class FixedIncome(SdkBaseModel):
    """Details about the fixed income security."""

    yield_rate: YieldRate | None
    """Details about a fixed income security's expected rate of return."""

    maturity_date: Date | None
    """The maturity date for this fixed income security, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format."""

    issue_date: Date | None
    """The issue date for this fixed income security, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    face_value: float | None
    """The face value that is paid upon maturity of the fixed income security, per unit of security."""


class FixedIncomeDict(TypedDict):
    yield_rate: YieldRate | YieldRateDict | None
    maturity_date: Date | None
    issue_date: Date | None
    face_value: float | None
