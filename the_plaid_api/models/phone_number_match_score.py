from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PhoneNumberMatchScore(SdkBaseModel):
    """Score found by matching phone number provided by the API with the phone number on the account at the financial
    institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match
    score is filled."""

    score: OptionalNullable[int] = UNSET
    """Match score for normalized phone number. 100 is a perfect match, 99-70 is a partial match (matching the same
    phone number with extension against one without extension, etc.), anything below 70 is considered a mismatch.
    Typically, the match threshold should be set to a score of 70 or higher. If the phone number is missing from either
    the API or financial institution, this is null."""


class PhoneNumberMatchScoreDict(TypedDict):
    score: NotRequired[int | None]
