from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .latest_scored_event import LatestScoredEvent, LatestScoredEventDict
from .protect_report import ProtectReport, ProtectReportDict


class ProtectUserInsightsGetResponse(SdkBaseModel):
    """Response object for /protect/user/insights/get"""

    user_id: str
    """The Plaid User ID. If a ``client_user_id`` was provided in the request instead of a ``user_id``, a new
    ``user_id`` will be generated if one doesn't already exist for that ``client_user_id``."""

    latest_scored_event: LatestScoredEvent | None
    """The latest scored event for a user."""

    reports: Optional[list[ProtectReport]] = UNSET
    """List of Protect reports associated with this user, limited to the most recent 100 reports in reverse
    chronological order (newest first)."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProtectUserInsightsGetResponseDict(TypedDict):
    user_id: str
    latest_scored_event: LatestScoredEventDict | None
    reports: NotRequired[list[ProtectReportDict]]
    request_id: str
