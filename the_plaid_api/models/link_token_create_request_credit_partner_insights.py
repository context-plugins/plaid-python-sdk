from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestCreditPartnerInsights(SdkBaseModel):
    """Specifies options for initializing Link for use with the Credit Partner Insights product."""

    days_requested: Optional[int] = UNSET
    """The maximum integer number of days of history to compute Credit Partner Insights. Defaults to 180 if not
    specified"""


class LinkTokenCreateRequestCreditPartnerInsightsDict(TypedDict):
    days_requested: NotRequired[int]
