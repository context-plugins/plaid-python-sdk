from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .document_risk_signal import DocumentRiskSignal, DocumentRiskSignalDict
from .risk_signal_document_reference import RiskSignalDocumentReference, RiskSignalDocumentReferenceDict


class MultiDocumentRiskSignal(SdkBaseModel):
    """Object containing risk signals and relevant metadata for a set of uploaded documents"""

    document_references: list[RiskSignalDocumentReference]
    """Array of objects containing attributes that could indicate if a document is fraudulent"""

    risk_signals: list[DocumentRiskSignal]
    """Array of attributes that indicate whether or not there is fraud risk with a set of documents"""


class MultiDocumentRiskSignalDict(TypedDict):
    document_references: list[RiskSignalDocumentReference | RiskSignalDocumentReferenceDict]
    risk_signals: list[DocumentRiskSignal | DocumentRiskSignalDict]
