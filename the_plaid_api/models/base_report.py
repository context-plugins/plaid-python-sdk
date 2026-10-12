from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .base_report_item import BaseReportItem, BaseReportItemDict
from .base_report_user_attributes import BaseReportUserAttributes, BaseReportUserAttributesDict


class BaseReport(SdkBaseModel):
    """An object representing a Base Report"""

    report_id: str
    """A unique ID identifying a Base Report. Like all Plaid identifiers, this ID is case sensitive."""

    date_generated: RFC3339DateTime
    """The date and time when the Base Report was created, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (e.g. "2018-04-12T03:32:11Z")."""

    days_requested: float
    """The number of days of transaction history requested."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    items: list[BaseReportItem]
    """Data returned by Plaid about each of the Items included in the Base Report."""

    attributes: Optional[BaseReportUserAttributes] = UNSET
    """Calculated attributes derived from transaction-level data, aggregated across accounts."""


class BaseReportDict(TypedDict):
    report_id: str
    date_generated: RFC3339DateTime
    days_requested: float
    client_report_id: NotRequired[str | None]
    items: list[BaseReportItemDict]
    attributes: NotRequired[BaseReportUserAttributesDict]
