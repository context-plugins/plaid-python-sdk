from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identity_document_upload import AccountIdentityDocumentUpload, AccountIdentityDocumentUploadDict
from .item import Item, ItemDict


class IdentityDocumentsUploadsGetResponse(SdkBaseModel):
    """IdentityDocumentsUploadsGetResponse defines the response schema for ``/identity/documents/uploads/get``"""

    accounts: list[AccountIdentityDocumentUpload]
    """The accounts for which Identity data has been requested"""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityDocumentsUploadsGetResponseDict(TypedDict):
    accounts: list[AccountIdentityDocumentUploadDict]
    item: ItemDict
    request_id: str
