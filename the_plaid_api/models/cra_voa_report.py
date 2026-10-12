from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_voa_report_attributes import CraVoaReportAttributes, CraVoaReportAttributesDict
from .cra_voa_report_item import CraVoaReportItem, CraVoaReportItemDict


class CraVoaReport(SdkBaseModel):
    """An object representing a VOA report."""

    generated_time: RFC3339DateTime
    """The date and time when the VOA Report was created, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (e.g. "2018-04-12T03:32:11Z")."""

    days_requested: float
    """The number of days of transaction history that the VOA report covers."""

    items: list[CraVoaReportItem]
    """Data returned by Plaid about each of the Items included in the Base Report."""

    attributes: CraVoaReportAttributes
    """Attributes for the VOA report."""


class CraVoaReportDict(TypedDict):
    generated_time: RFC3339DateTime
    days_requested: float
    items: list[CraVoaReportItemDict]
    attributes: CraVoaReportAttributesDict
