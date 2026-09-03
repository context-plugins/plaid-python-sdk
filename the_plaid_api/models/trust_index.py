from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .trust_index_subscores import TrustIndexSubscores, TrustIndexSubscoresDict


class TrustIndex(SdkBaseModel):
    """Represents a calculated Trust Index Score."""

    score: int
    """The overall trust index score."""

    model: str
    """The versioned name of the Trust Index model used for scoring."""

    subscores: TrustIndexSubscores | None
    """Contains sub-score metadata."""


class TrustIndexDict(TypedDict):
    score: int
    model: str
    subscores: TrustIndexSubscores | TrustIndexSubscoresDict | None
