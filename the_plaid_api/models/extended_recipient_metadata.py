from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class ExtendedRecipientMetadata(SdkBaseModel):
    """Plaid and FDX-defined recipient metadata fields"""

    recipient_id: str
    """The recipient identifier"""

    client_name: str
    """The recipient name displayed by the Data Provider during the consent flow"""

    logo_uri: OptionalNullable[str] = UNSET
    """Data Recipient Logo URL location"""

    third_party_legal_name: str
    """The legal name of the recipient"""

    category: str
    """The category that the recipient falls under"""

    joined_date: Date
    """The date at which the recipient gained production access to Plaid"""

    connection_count: int
    """The number of consumers connected to the recipient through this Data Partner"""


class ExtendedRecipientMetadataDict(TypedDict):
    recipient_id: str
    client_name: str
    logo_uri: NotRequired[str | None]
    third_party_legal_name: str
    category: str
    joined_date: Date
    connection_count: int
