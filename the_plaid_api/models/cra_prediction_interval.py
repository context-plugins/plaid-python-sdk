from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CraPredictionInterval(SdkBaseModel):
    """The object containing prediction interval data."""

    lower_bound: OptionalNullable[float] = UNSET
    """The lower bound of the predicted attribute for the given probability."""

    upper_bound: OptionalNullable[float] = UNSET
    """The upper bound of the predicted attribute for the given probability."""

    probability: OptionalNullable[float] = UNSET
    """The probability of the actual value of the attribute falling within the upper and lower bound. This is a
    percentage represented as a value between 0 and 1."""


class CraPredictionIntervalDict(TypedDict):
    lower_bound: NotRequired[float | None]
    upper_bound: NotRequired[float | None]
    probability: NotRequired[float | None]
