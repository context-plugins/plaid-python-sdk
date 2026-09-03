from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class IdentityDocumentUploadMetadata(SdkBaseModel):
    """Metadata pertaining to the document."""

    document_type: OptionalNullable[str] = UNSET
    """The submitted document type. Currently, this will always be ``BANK_STATEMENT``."""

    is_account_number_match: OptionalNullable[bool] = UNSET
    """Boolean field indicating whether the uploaded document's account number matches the account number we have on
    file. If ``false``, it is not recommended to accept the uploaded identity data as accurate without further
    verification."""

    page_count: OptionalNullable[int] = UNSET
    """The number of pages in the uploaded document."""

    last_updated: Optional[RFC3339DateTime] = UNSET
    """The timestamp when the document was last updated."""

    uploaded_at: Optional[RFC3339DateTime] = UNSET
    """The timestamp when the document was originally uploaded."""


class IdentityDocumentUploadMetadataDict(TypedDict):
    document_type: NotRequired[str | None]
    is_account_number_match: NotRequired[bool | None]
    page_count: NotRequired[int | None]
    last_updated: NotRequired[RFC3339DateTime]
    uploaded_at: NotRequired[RFC3339DateTime]
