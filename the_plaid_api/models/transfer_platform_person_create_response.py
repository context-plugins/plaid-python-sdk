from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferPlatformPersonCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/platform/person/create``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    person_id: str
    """An ID that should be used when submitting additional requirements that are associated with this person."""


class TransferPlatformPersonCreateResponseDict(TypedDict):
    request_id: str
    person_id: str
