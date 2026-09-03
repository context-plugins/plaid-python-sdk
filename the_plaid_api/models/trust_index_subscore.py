from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TrustIndexSubscore(SdkBaseModel):
    """Represents Trust Index Subscore."""

    score: int
    """The subscore score."""


class TrustIndexSubscoreDict(TypedDict):
    score: int
