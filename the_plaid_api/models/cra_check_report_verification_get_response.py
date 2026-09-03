from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_report_warning import CraReportWarning, CraReportWarningDict
from .cra_verification_report import CraVerificationReport, CraVerificationReportDict


class CraCheckReportVerificationGetResponse(SdkBaseModel):
    """CraCheckReportVerificationGetResponse defines the response schema for ``/cra/check_report/verification/get``."""

    report: CraVerificationReport
    """Contains data for the CRA Home Lending Report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    warnings: list[CraReportWarning]
    """If the home lending report generation was successful but a subset of data could not be retrieved, this array will
    contain information about the errors causing information to be missing."""


class CraCheckReportVerificationGetResponseDict(TypedDict):
    report: CraVerificationReport | CraVerificationReportDict
    request_id: str
    warnings: list[CraReportWarning | CraReportWarningDict]
