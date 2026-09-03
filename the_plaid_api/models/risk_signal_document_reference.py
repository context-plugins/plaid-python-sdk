from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.risk_signal_document_status import RiskSignalDocumentStatusOrStr
from .enums.risk_signal_document_type import RiskSignalDocumentTypeOrStr
from .enums.risk_signal_file_type import RiskSignalFileTypeOrStr


class RiskSignalDocumentReference(SdkBaseModel):
    """Object containing metadata for the document"""

    document_id: OptionalNullable[str] = UNSET
    """An identifier of the document referenced by the document metadata."""

    document_name: Optional[str] = UNSET
    """The name of the document"""

    status: Optional[RiskSignalDocumentStatusOrStr] = UNSET
    """Status of a document for risk signal analysis"""

    document_type: OptionalNullable[RiskSignalDocumentTypeOrStr] = UNSET
    """Type of a document for risk signal analysis"""

    file_type: OptionalNullable[RiskSignalFileTypeOrStr] = UNSET
    """The file type for risk signal analysis"""


class RiskSignalDocumentReferenceDict(TypedDict):
    document_id: NotRequired[str | None]
    document_name: NotRequired[str]
    status: NotRequired[RiskSignalDocumentStatusOrStr]
    document_type: NotRequired[RiskSignalDocumentTypeOrStr | None]
    file_type: NotRequired[RiskSignalFileTypeOrStr | None]
