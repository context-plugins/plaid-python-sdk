from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IssuesSubscribeResponse(SdkBaseModel):
    """IssuesSubscribeResponse defines the response schema for ``/issues/subscribe``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IssuesSubscribeResponseDict(TypedDict):
    request_id: str
