from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.cashflow_attributes_version import CashflowAttributesVersionOrStr


class CraCheckReportCashflowInsightsGetOptions(SdkBaseModel):
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``options``."""

    attributes_version: OptionalNullable[CashflowAttributesVersionOrStr] = UNSET
    """The version of cashflow attributes. Required if using Cash Flow Insights."""


class CraCheckReportCashflowInsightsGetOptionsDict(TypedDict):
    attributes_version: NotRequired[CashflowAttributesVersionOrStr | None]
