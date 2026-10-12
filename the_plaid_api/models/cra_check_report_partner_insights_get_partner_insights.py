from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .cra_partner_insights_fico_input import CraPartnerInsightsFicoInput, CraPartnerInsightsFicoInputDict
from .prism_versions import PrismVersions, PrismVersionsDict


class CraCheckReportPartnerInsightsGetPartnerInsights(SdkBaseModel):
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``partner_insights``."""

    prism_versions: OptionalNullable[PrismVersions] = UNSET
    """The versions of Prism products to evaluate"""

    fico: OptionalNullable[CraPartnerInsightsFicoInput] = UNSET
    """Configuration for the FICO products used in the Partner Insights product."""


class CraCheckReportPartnerInsightsGetPartnerInsightsDict(TypedDict):
    prism_versions: NotRequired[PrismVersionsDict | None]
    fico: NotRequired[CraPartnerInsightsFicoInputDict | None]
