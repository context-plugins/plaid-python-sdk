from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .multi_document_risk_signal import MultiDocumentRiskSignal, MultiDocumentRiskSignalDict
from .single_document_risk_signal import SingleDocumentRiskSignal, SingleDocumentRiskSignalDict


class DocumentRiskSignalsObject(SdkBaseModel):
    """Object containing fraud risk data for a set of income documents."""

    account_id: str | None
    """ID of the payroll provider account."""

    single_document_risk_signals: list[SingleDocumentRiskSignal]
    """Array of document metadata and associated risk signals per document"""

    multi_document_risk_signals: list[MultiDocumentRiskSignal]
    """Array of risk signals computed from a set of uploaded documents and the associated documents' metadata"""


class DocumentRiskSignalsObjectDict(TypedDict):
    account_id: str | None
    single_document_risk_signals: list[SingleDocumentRiskSignalDict]
    multi_document_risk_signals: list[MultiDocumentRiskSignalDict]
