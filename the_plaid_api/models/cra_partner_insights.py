from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .cra_partner_insights_fico_results import CraPartnerInsightsFicoResults, CraPartnerInsightsFicoResultsDict
from .cra_partner_insights_item import CraPartnerInsightsItem, CraPartnerInsightsItemDict
from .cra_partner_insights_prism import CraPartnerInsightsPrism, CraPartnerInsightsPrismDict


class CraPartnerInsights(SdkBaseModel):
    """The Partner Insights report of the bank data for an end user."""

    report_id: Optional[str] = UNSET
    """A unique identifier associated with the Partner Insights object."""

    generated_time: Optional[RFC3339DateTime] = UNSET
    """The time when the Partner Insights report was generated."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    fico: OptionalNullable[CraPartnerInsightsFicoResults] = UNSET
    """The calculated UltraFICO® scores returned as part of the Partner Insights report."""

    prism: OptionalNullable[CraPartnerInsightsPrism] = UNSET
    """The Prism Data insights for the user."""

    items: Optional[list[CraPartnerInsightsItem]] = UNSET
    """The list of Items used in the report along with the associated metadata about the Item."""


class CraPartnerInsightsDict(TypedDict):
    report_id: NotRequired[str]
    generated_time: NotRequired[RFC3339DateTime]
    client_report_id: NotRequired[str | None]
    fico: NotRequired[CraPartnerInsightsFicoResultsDict | None]
    prism: NotRequired[CraPartnerInsightsPrismDict | None]
    items: NotRequired[list[CraPartnerInsightsItemDict]]
