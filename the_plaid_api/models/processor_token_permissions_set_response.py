from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorTokenPermissionsSetResponse(SdkBaseModel):
    """ProcessorTokenPermissionsSetResponse defines the response schema for ``/processor/token/permissions/set``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorTokenPermissionsSetResponseDict(TypedDict):
    request_id: str
