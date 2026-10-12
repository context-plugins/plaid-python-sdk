from __future__ import annotations

from typing_extensions import TypedDict

from ..core import FileResponse, SdkBaseModel
from .enums.purpose import PurposeOrStr


class TransferDiligenceDocumentUploadRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/diligence/document/upload``"""

    originator_client_id: str
    """The Client ID of the originator whose document that you want to upload."""

    file: FileResponse
    """A file to upload. The file size must be less than 20MB. Supported file extensions: .pdf."""

    purpose: PurposeOrStr
    """Specifies the purpose of the uploaded file.

    ``"DUE_DILIGENCE"`` - The transfer due diligence document of the originator."""


class TransferDiligenceDocumentUploadRequestDict(TypedDict):
    originator_client_id: str
    file: FileResponse
    purpose: PurposeOrStr
