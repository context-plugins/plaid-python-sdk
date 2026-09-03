from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.cashflow_attributes_version import CashflowAttributesVersionOrStr


class LinkTokenCreateRequestCraOptionsCashflowInsights(SdkBaseModel):
    """Specifies options for initializing Link for use with the Cashflow Insights product."""

    attributes_version: OptionalNullable[CashflowAttributesVersionOrStr] = UNSET
    """The version of cashflow attributes. Required if using Cash Flow Insights."""


class LinkTokenCreateRequestCraOptionsCashflowInsightsDict(TypedDict):
    attributes_version: NotRequired[CashflowAttributesVersionOrStr | None]
