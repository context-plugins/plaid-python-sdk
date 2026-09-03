from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .document_analysis import DocumentAnalysis, DocumentAnalysisDict
from .enums.document_status import DocumentStatusOrStr
from .physical_document_extracted_data import PhysicalDocumentExtractedData, PhysicalDocumentExtractedDataDict
from .physical_document_images import PhysicalDocumentImages, PhysicalDocumentImagesDict


class DocumentaryVerificationDocument(SdkBaseModel):
    """Images, extracted data, and analysis from a user's identity document"""

    status: DocumentStatusOrStr
    """An outcome status for this specific document submission. Distinct from the overall
    ``documentary_verification.status`` that summarizes the verification outcome from one or more documents."""

    attempt: int
    """The ``attempt`` field begins with 1 and increments with each subsequent document upload."""

    images: PhysicalDocumentImages
    """URLs for downloading original and cropped images for this document submission. The URLs are designed to only
    allow downloading, not hot linking, so the URL will only serve the document image for 60 seconds before expiring.
    The expiration time is 60 seconds after the ``GET`` request for the associated Identity Verification attempt. A new
    expiring URL is generated with each request, so you can always rerequest the Identity Verification attempt if one of
    your URLs expires."""

    extracted_data: PhysicalDocumentExtractedData | None
    """Data extracted from a user-submitted document."""

    analysis: DocumentAnalysis
    """High level descriptions of how the associated document was processed. If a document fails verification, the
    details in the ``analysis`` object should help clarify why the document was rejected."""

    redacted_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""


class DocumentaryVerificationDocumentDict(TypedDict):
    status: DocumentStatusOrStr
    attempt: int
    images: PhysicalDocumentImages | PhysicalDocumentImagesDict
    extracted_data: PhysicalDocumentExtractedData | PhysicalDocumentExtractedDataDict | None
    analysis: DocumentAnalysis | DocumentAnalysisDict
    redacted_at: RFC3339DateTime | None
