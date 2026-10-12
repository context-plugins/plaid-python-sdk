from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .ewa_score import EwaScore, EwaScoreDict


class BetaEwaReportV1GetResponse(SdkBaseModel):
    """BetaEwaReportV1GetResponse defines the response schema for ``/beta/ewa_report/v1/get``"""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    ewa_report_id: Optional[str] = UNSET
    """Unique identifier for the generated EWA score group."""

    generation_time: Optional[RFC3339DateTime] = UNSET
    """The date and time when ``ewa_scores`` was generated, in ISO 8601 format (e.g. "2018-04-12T03:32:11Z")."""

    ewa_scores: Optional[list[EwaScore]] = UNSET
    """A list of earned wage access (EWA) scoring entries that map potential advance amounts to repayment likelihood
    scores. The predefined advance amount ranges are ``[0, 25)``, ``[25, 50)``, ``[50, 100)``, ``[100, 200)``, ``[200,
    300)``, ``[300, 400)``, and ``[400, 500)``."""

    ewa_attributes: OptionalNullable[dict[str, float | None]] = UNSET
    """A set of attributes providing context about the factors that contributed to the EWA scores. Each key is the
    attribute name and the value is its numeric score, or null if the attribute could not be computed."""


class BetaEwaReportV1GetResponseDict(TypedDict):
    request_id: NotRequired[str]
    ewa_report_id: NotRequired[str]
    generation_time: NotRequired[RFC3339DateTime]
    ewa_scores: NotRequired[list[EwaScoreDict]]
    ewa_attributes: NotRequired[dict[str, float | None] | None]
