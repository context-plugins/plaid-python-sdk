from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_lend_score_report import CraLendScoreReport, CraLendScoreReportDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCheckReportLendScoreGetResponse(SdkBaseModel):
    """CraCheckReportLendScoreGetResponse defines the response schema for ``/cra/check_report/lend_score/get``."""

    report: CraLendScoreReport
    """Contains data for the CRA LendScore Report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: Optional[list[CraReportWarning]] = UNSET
    """If the LendScore generation was successful but a subset of data could not be retrieved, this array will contain
    information about the errors causing information to be missing"""


class CraCheckReportLendScoreGetResponseDict(TypedDict):
    report: CraLendScoreReportDict
    request_id: str
    warnings: NotRequired[list[CraReportWarningDict]]
