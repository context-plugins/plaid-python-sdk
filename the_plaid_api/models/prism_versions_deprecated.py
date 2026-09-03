from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.prism_cash_score_version import PrismCashScoreVersionOrStr
from .enums.prism_detect_version import PrismDetectVersionOrStr
from .enums.prism_extend_version import PrismExtendVersionOrStr
from .enums.prism_first_detect_version import PrismFirstDetectVersionOrStr
from .enums.prism_insights_version import PrismInsightsVersionOrStr


class PrismVersionsDeprecated(SdkBaseModel):
    """Deprecated, use ``partner_insights.prism_versions`` instead."""

    firstdetect: OptionalNullable[PrismFirstDetectVersionOrStr] = UNSET
    """The version of Prism FirstDetect. If not specified, will default to v3."""

    detect: OptionalNullable[PrismDetectVersionOrStr] = UNSET
    """The version of Prism Detect"""

    cashscore: OptionalNullable[PrismCashScoreVersionOrStr] = UNSET
    """The version of Prism CashScore. If not specified, will default to v3."""

    extend: OptionalNullable[PrismExtendVersionOrStr] = UNSET
    """The version of Prism Extend"""

    insights: OptionalNullable[PrismInsightsVersionOrStr] = UNSET
    """The version of Prism Insights. If not specified, will default to v3."""


class PrismVersionsDeprecatedDict(TypedDict):
    firstdetect: NotRequired[PrismFirstDetectVersionOrStr | None]
    detect: NotRequired[PrismDetectVersionOrStr | None]
    cashscore: NotRequired[PrismCashScoreVersionOrStr | None]
    extend: NotRequired[PrismExtendVersionOrStr | None]
    insights: NotRequired[PrismInsightsVersionOrStr | None]
