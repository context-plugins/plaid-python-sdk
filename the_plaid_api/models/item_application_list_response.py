from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .connected_application import ConnectedApplication, ConnectedApplicationDict


class ItemApplicationListResponse(SdkBaseModel):
    """Describes the connected application for a particular end user."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    applications: list[ConnectedApplication]
    """A list of connected applications."""


class ItemApplicationListResponseDict(TypedDict):
    request_id: NotRequired[str]
    applications: list[ConnectedApplicationDict]
