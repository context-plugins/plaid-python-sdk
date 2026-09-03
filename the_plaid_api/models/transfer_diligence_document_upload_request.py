from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class TransferDiligenceDocumentUploadRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/diligence/document/upload``"""

    originator_client_id: str
    """The Client ID of the originator whose document that you want to upload."""

    file: bytes
    """A file to upload. The file size must be less than 20MB. Supported file extensions: .pdf."""

    purpose: Literal["DUE_DILIGENCE"] = "DUE_DILIGENCE"
    """Specifies the purpose of the uploaded file.

    ``"DUE_DILIGENCE"`` - The transfer due diligence document of the originator."""


class TransferDiligenceDocumentUploadRequestDict(TypedDict):
    originator_client_id: str
    file: bytes
    purpose: NotRequired[Literal["DUE_DILIGENCE"]]
