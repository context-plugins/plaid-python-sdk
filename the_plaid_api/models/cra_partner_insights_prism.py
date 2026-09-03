from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .prism_cash_score import PrismCashScore, PrismCashScoreDict
from .prism_detect import PrismDetect, PrismDetectDict
from .prism_extend import PrismExtend, PrismExtendDict
from .prism_first_detect import PrismFirstDetect, PrismFirstDetectDict
from .prism_insights import PrismInsights, PrismInsightsDict


class CraPartnerInsightsPrism(SdkBaseModel):
    """The Prism Data insights for the user."""

    insights: OptionalNullable[PrismInsights] = UNSET
    """The data from the Insights product returned by Prism Data."""

    cash_score: OptionalNullable[PrismCashScore] = UNSET
    """The data from the CashScore® product returned by Prism Data."""

    extend: OptionalNullable[PrismExtend] = UNSET
    """The data from the CashScore® Extend product returned by Prism Data."""

    first_detect: OptionalNullable[PrismFirstDetect] = UNSET
    """The data from the FirstDetect product returned by Prism Data."""

    detect: OptionalNullable[PrismDetect] = UNSET
    """The data from the CashScore® Detect product returned by Prism Data."""

    status: str
    """Details on whether the Prism Data attributes succeeded or failed to be generated."""


class CraPartnerInsightsPrismDict(TypedDict):
    insights: NotRequired[PrismInsights | PrismInsightsDict | None]
    cash_score: NotRequired[PrismCashScore | PrismCashScoreDict | None]
    extend: NotRequired[PrismExtend | PrismExtendDict | None]
    first_detect: NotRequired[PrismFirstDetect | PrismFirstDetectDict | None]
    detect: NotRequired[PrismDetect | PrismDetectDict | None]
    status: str
