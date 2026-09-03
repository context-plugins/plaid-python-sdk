from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class NameMatchScore(SdkBaseModel):
    """Score found by matching name provided by the API with the name on the account at the financial institution. If
    the account contains multiple owners, the maximum match score is filled."""

    score: OptionalNullable[int] = UNSET
    """Match score for name. 100 is a perfect score, 99-85 means a strong match, 84-70 is a partial match, any score
    less than 70 is a mismatch. Typically, the match threshold should be set to a score of 70 or higher. If the name is
    missing from either the API or financial institution, this is null."""

    is_first_name_or_last_name_match: OptionalNullable[bool] = UNSET
    """first or last name completely matched, likely a family member"""

    is_nickname_match: OptionalNullable[bool] = UNSET
    """nickname matched, example Jennifer and Jenn."""

    is_business_name_detected: OptionalNullable[bool] = UNSET
    """Is ``true`` if the name on either of the names that was matched for the score contained strings indicative of a
    business name, such as "CORP", "LLC", "INC", or "LTD". A ``true`` result generally indicates that an account's name
    is a business name. However, a ``false`` result does not mean the account name is not a business name, as some
    businesses do not use these strings in the names used for their financial institution accounts."""


class NameMatchScoreDict(TypedDict):
    score: NotRequired[int | None]
    is_first_name_or_last_name_match: NotRequired[bool | None]
    is_nickname_match: NotRequired[bool | None]
    is_business_name_detected: NotRequired[bool | None]
