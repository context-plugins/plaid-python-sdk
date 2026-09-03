from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorTokenCreateResponse(SdkBaseModel):
    """ProcessorTokenCreateResponse defines the response schema for ``/processor/token/create`` and
    ``/processor/apex/processor_token/create``"""

    processor_token: str
    """The ``processor_token`` that can then be used by the Plaid partner to make API requests"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorTokenCreateResponseDict(TypedDict):
    processor_token: str
    request_id: str
