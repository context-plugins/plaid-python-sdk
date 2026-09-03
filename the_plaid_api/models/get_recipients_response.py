from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .extended_recipient_metadata import ExtendedRecipientMetadata, ExtendedRecipientMetadataDict


class GetRecipientsResponse(SdkBaseModel):
    """GetRecipientsResponse defines the response schema for ``/fdx/recipients``"""

    recipients: list[ExtendedRecipientMetadata]


class GetRecipientsResponseDict(TypedDict):
    recipients: list[ExtendedRecipientMetadata | ExtendedRecipientMetadataDict]
