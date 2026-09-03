from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class IdentityDocumentMetadata(SdkBaseModel):
    """In closed beta. Object representing metadata pertaining to the document."""

    is_account_number_match: Optional[bool] = UNSET
    """Boolean field indicating if the uploaded document's account number matches the account number we have on file"""

    last_updated: Optional[RFC3339DateTime] = UNSET
    uploaded_at: Optional[RFC3339DateTime] = UNSET


class IdentityDocumentMetadataDict(TypedDict):
    is_account_number_match: NotRequired[bool]
    last_updated: NotRequired[RFC3339DateTime]
    uploaded_at: NotRequired[RFC3339DateTime]
