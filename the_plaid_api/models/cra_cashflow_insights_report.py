from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CraCashflowInsightsReport(SdkBaseModel):
    """Contains data for the CRA Cashflow Insights Report."""

    report_id: str
    """The unique identifier associated with the report object."""

    generated_time: RFC3339DateTime
    """The time when the report was generated."""

    attributes: Optional[Any] = UNSET
    """A map of cash flow attributes, where the key is a string, and the value is a string, float, int, or boolean. The
    specific list of attributes will depend on the cash flow attributes version used. For a full list of attributes,
    contact your account manager."""


class CraCashflowInsightsReportDict(TypedDict):
    report_id: str
    generated_time: RFC3339DateTime
    attributes: NotRequired[Any]
