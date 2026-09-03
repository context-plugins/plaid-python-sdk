from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.human_review_status import HumanReviewStatusOrStr


class HumanReview(SdkBaseModel):
    """Details about the human review check, which refers to a check that is performed by a document specialist."""

    status: HumanReviewStatusOrStr
    """The outcome of the human review check, when available. The following values are possible:


    ``success`` - The document passed the check.

    ``failed`` - The document failed the check.

    ``no_data`` - The document was submitted, but the document specialist review was not completed in time."""


class HumanReviewDict(TypedDict):
    status: HumanReviewStatusOrStr
