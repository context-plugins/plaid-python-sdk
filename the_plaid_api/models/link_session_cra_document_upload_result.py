from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkSessionCraDocumentUploadResult(SdkBaseModel):
    """The details of a document upload CRA session in Link"""

    num_bank_statements_uploaded: int
    """The number of bank statements uploaded by the user."""


class LinkSessionCraDocumentUploadResultDict(TypedDict):
    num_bank_statements_uploaded: int
