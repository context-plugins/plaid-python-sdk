from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .prism_versions_deprecated import PrismVersionsDeprecated, PrismVersionsDeprecatedDict


class CraCheckReportPartnerInsightsGetOptions(SdkBaseModel):
    """Deprecated, specify ``partner_insights.prism_versions`` instead."""

    prism_versions: OptionalNullable[PrismVersionsDeprecated] = UNSET
    """Deprecated, use ``partner_insights.prism_versions`` instead."""


class CraCheckReportPartnerInsightsGetOptionsDict(TypedDict):
    prism_versions: NotRequired[PrismVersionsDeprecatedDict | None]
