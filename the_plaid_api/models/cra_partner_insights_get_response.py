from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_partner_insights import CraPartnerInsights, CraPartnerInsightsDict


class CraPartnerInsightsGetResponse(SdkBaseModel):
    """CraPartnerInsightsGetResponse defines the response schema for ``/cra/partner_insights/get``."""

    report: Optional[list[CraPartnerInsights]] = UNSET
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraPartnerInsightsGetResponseDict(TypedDict):
    report: NotRequired[list[CraPartnerInsights | CraPartnerInsightsDict]]
    request_id: str
