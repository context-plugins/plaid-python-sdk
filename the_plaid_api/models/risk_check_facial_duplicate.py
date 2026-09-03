from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RiskCheckFacialDuplicate(SdkBaseModel):
    """Result summary object specifying values for the ``facial_duplicates`` attributes of risk check."""

    id: str
    """ID of the associated Identity Verification attempt."""

    similarity: int
    """Similarity score of the match. Ranges from 0 to 100."""

    matched_after_completed: bool
    """Whether this match occurred after the session was complete. For example, this would be ``true`` if a later
    session ended up matching this one."""


class RiskCheckFacialDuplicateDict(TypedDict):
    id: str
    similarity: int
    matched_after_completed: bool
