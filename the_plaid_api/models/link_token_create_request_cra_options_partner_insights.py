from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_partner_insights_fico_input import CraPartnerInsightsFicoInput, CraPartnerInsightsFicoInputDict
from .prism_versions import PrismVersions, PrismVersionsDict


class LinkTokenCreateRequestCraOptionsPartnerInsights(SdkBaseModel):
    """Specifies options for initializing Link for use with the Credit Partner Insights product."""

    prism_versions: OptionalNullable[PrismVersions] = UNSET
    """The versions of Prism products to evaluate"""

    fico: OptionalNullable[CraPartnerInsightsFicoInput] = UNSET
    """Configuration for the FICO products used in the Partner Insights product."""


class LinkTokenCreateRequestCraOptionsPartnerInsightsDict(TypedDict):
    prism_versions: NotRequired[PrismVersions | PrismVersionsDict | None]
    fico: NotRequired[CraPartnerInsightsFicoInput | CraPartnerInsightsFicoInputDict | None]
