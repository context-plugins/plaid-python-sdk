from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .identity_document_upload_metadata import IdentityDocumentUploadMetadata, IdentityDocumentUploadMetadataDict
from .identity_document_upload_risk_insights import (
    IdentityDocumentUploadRiskInsights,
    IdentityDocumentUploadRiskInsightsDict,
)


class IdentityDocumentUpload(SdkBaseModel):
    """Document object with metadata of the uploaded document"""

    document_id: Optional[str] = UNSET
    """A UUID identifying the document."""

    metadata: Optional[IdentityDocumentUploadMetadata] = UNSET
    """Metadata pertaining to the document."""

    risk_insights: Optional[IdentityDocumentUploadRiskInsights] = UNSET
    """Object representing fraud risk data of the uploaded document. Only provided when using Identity Document Upload
    with Fraud Risk enabled."""


class IdentityDocumentUploadDict(TypedDict):
    document_id: NotRequired[str]
    metadata: NotRequired[IdentityDocumentUploadMetadataDict]
    risk_insights: NotRequired[IdentityDocumentUploadRiskInsightsDict]
