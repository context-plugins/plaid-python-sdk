from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.user_stated_income_source_category import UserStatedIncomeSourceCategoryOrStr
from .enums.user_stated_income_source_frequency import UserStatedIncomeSourceFrequencyOrStr
from .enums.user_stated_income_source_pay_type import UserStatedIncomeSourcePayTypeOrStr


class LinkTokenCreateRequestUserStatedIncomeSource(SdkBaseModel):
    """Specifies user stated income sources for the Income product"""

    employer: Optional[str] = UNSET
    """The employer corresponding to an income source specified by the user"""

    category: Optional[UserStatedIncomeSourceCategoryOrStr] = UNSET
    """The income category for a specified income source"""

    pay_per_cycle: Optional[float] = UNSET
    """The income amount paid per cycle for a specified income source"""

    pay_annual: Optional[float] = UNSET
    """The income amount paid annually for a specified income source"""

    pay_type: Optional[UserStatedIncomeSourcePayTypeOrStr] = UNSET
    """The pay type - ``GROSS``, ``NET``, or ``UNKNOWN`` for a specified income source"""

    pay_frequency: Optional[UserStatedIncomeSourceFrequencyOrStr] = UNSET
    """The pay frequency of a specified income source"""


class LinkTokenCreateRequestUserStatedIncomeSourceDict(TypedDict):
    employer: NotRequired[str]
    category: NotRequired[UserStatedIncomeSourceCategoryOrStr]
    pay_per_cycle: NotRequired[float]
    pay_annual: NotRequired[float]
    pay_type: NotRequired[UserStatedIncomeSourcePayTypeOrStr]
    pay_frequency: NotRequired[UserStatedIncomeSourceFrequencyOrStr]
