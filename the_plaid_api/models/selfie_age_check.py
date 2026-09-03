from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.selfie_age_check_status import SelfieAgeCheckStatusOrStr


class SelfieAgeCheck(SdkBaseModel):
    """Age-estimation results from the selfie capture. This field is ``null`` when an age range could not be estimated
    from the selfie capture."""

    status: SelfieAgeCheckStatusOrStr
    """An enum indicating whether the reported age aligns with the estimated selfie capture age range.

    ``match`` indicates that the reported age falls within the estimated selfie capture age range.

    ``warning`` indicates that the reported age falls outside the estimated selfie capture age range, but is close
    enough that the result should be reviewed.

    ``no_match`` indicates that the reported age falls far outside the estimated selfie capture age range.

    ``no_data`` indicates that there was not enough data available at age-estimation time to compare the reported age
    against the estimated selfie capture age range."""

    reported_age: int | None
    """The user's age at the time of the selfie capture, calculated from the date of birth submitted during Identity
    Verification. If multiple date of birth sources are available, the date of birth submitted in the flow session takes
    priority over the document date of birth. This field is ``null`` when the date of birth is unavailable."""

    age_estimate_lower_bound: int
    """Lower bound of the estimated age range from the selfie capture."""

    age_estimate_upper_bound: int
    """Upper bound of the estimated age range from the selfie capture."""


class SelfieAgeCheckDict(TypedDict):
    status: SelfieAgeCheckStatusOrStr
    reported_age: int | None
    age_estimate_lower_bound: int
    age_estimate_upper_bound: int
