from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .identity_document_upload_risk_signal import IdentityDocumentUploadRiskSignal, IdentityDocumentUploadRiskSignalDict
from .identity_document_upload_risk_summary import (
    IdentityDocumentUploadRiskSummary,
    IdentityDocumentUploadRiskSummaryDict,
)


class IdentityDocumentUploadRiskInsights(SdkBaseModel):
    """Object representing fraud risk data of the uploaded document. Only provided when using Identity Document Upload
    with Fraud Risk enabled."""

    risk_summary: Optional[IdentityDocumentUploadRiskSummary] = UNSET
    """Risk summary of an uploaded document."""

    risk_signals: Optional[list[IdentityDocumentUploadRiskSignal]] = UNSET
    """An array of risk signals."""


class IdentityDocumentUploadRiskInsightsDict(TypedDict):
    risk_summary: NotRequired[IdentityDocumentUploadRiskSummaryDict]
    risk_signals: NotRequired[list[IdentityDocumentUploadRiskSignalDict]]
