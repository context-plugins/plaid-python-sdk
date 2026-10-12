from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .document_risk_signals_object import DocumentRiskSignalsObject, DocumentRiskSignalsObjectDict


class PayrollRiskSignalsItem(SdkBaseModel):
    """Object containing fraud risk data pertaining to the Item linked as part of the verification."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    verification_risk_signals: list[DocumentRiskSignalsObject]
    """Array of payroll income document authenticity data retrieved for each of the user's accounts."""


class PayrollRiskSignalsItemDict(TypedDict):
    item_id: str
    verification_risk_signals: list[DocumentRiskSignalsObjectDict]
