from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FdxrecipientMetadata(SdkBaseModel):
    """Recipient metadata fields that are defined by FDX."""

    recipient_id: str
    """The recipient identifier"""

    client_name: str
    """The recipient name displayed by the Data Provider during the consent flow"""

    logo_uri: OptionalNullable[str] = UNSET
    """Data Recipient Logo URL location"""

    third_party_legal_name: str
    """The legal name of the recipient"""


class FdxrecipientMetadataDict(TypedDict):
    recipient_id: str
    client_name: str
    logo_uri: NotRequired[str | None]
    third_party_legal_name: str
