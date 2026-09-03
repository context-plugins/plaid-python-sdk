from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .account_insights import AccountInsights, AccountInsightsDict
from .asset_report_item import AssetReportItem, AssetReportItemDict
from .asset_report_user import AssetReportUser, AssetReportUserDict


class AssetReport(SdkBaseModel):
    """An object representing an Asset Report"""

    asset_report_id: str
    """A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""

    insights: OptionalNullable[AccountInsights] = UNSET
    """This is a container object for all lending-related insights. This field will be returned only for European
    customers."""

    client_report_id: str | None
    """An identifier you determine and submit for the Asset Report."""

    date_generated: RFC3339DateTime
    """The date and time when the Asset Report was created, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (e.g. "2018-04-12T03:32:11Z")."""

    days_requested: float
    """The duration of transaction history you requested"""

    user: AssetReportUser
    """The user object allows you to provide additional information about the user to be appended to the Asset Report.
    All fields are optional. The ``first_name``, ``last_name``, and ``ssn`` fields are required if you would like the
    Report to be eligible for Fannie Mae's Day 1 Certainty™ program."""

    items: list[AssetReportItem]
    """Data returned by Plaid about each of the Items included in the Asset Report."""


class AssetReportDict(TypedDict):
    asset_report_id: str
    insights: NotRequired[AccountInsights | AccountInsightsDict | None]
    client_report_id: str | None
    date_generated: RFC3339DateTime
    days_requested: float
    user: AssetReportUser | AssetReportUserDict
    items: list[AssetReportItem | AssetReportItemDict]
