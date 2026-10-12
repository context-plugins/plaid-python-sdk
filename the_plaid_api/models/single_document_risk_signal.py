from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .document_risk_signal import DocumentRiskSignal, DocumentRiskSignalDict
from .document_risk_summary import DocumentRiskSummary, DocumentRiskSummaryDict
from .risk_signal_document_reference import RiskSignalDocumentReference, RiskSignalDocumentReferenceDict


class SingleDocumentRiskSignal(SdkBaseModel):
    """Object containing all risk signals and relevant metadata for a single document"""

    document_reference: RiskSignalDocumentReference
    """Object containing metadata for the document"""

    risk_signals: list[DocumentRiskSignal | None]
    """Array of attributes that indicate whether or not there is fraud risk with a document"""

    risk_summary: DocumentRiskSummary
    """A summary across all risk signals associated with a document"""


class SingleDocumentRiskSignalDict(TypedDict):
    document_reference: RiskSignalDocumentReferenceDict
    risk_signals: list[DocumentRiskSignalDict | None]
    risk_summary: DocumentRiskSummaryDict
