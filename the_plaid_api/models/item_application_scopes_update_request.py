from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.scopes_context import ScopesContextOrStr
from .scopes import Scopes, ScopesDict


class ItemApplicationScopesUpdateRequest(SdkBaseModel):
    """ItemApplicationScopesUpdateRequest defines the request schema for ``/item/application/scopes/update``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    application_id: str
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""

    scopes: Scopes
    """The scopes object"""

    state: Optional[str] = UNSET
    """When scopes are updated during enrollment, this field must be populated with the state sent to the partner in the
    OAuth Login URI. This field is required when the context is ``ENROLLMENT``."""

    context: ScopesContextOrStr
    """An indicator for when scopes are being updated. When scopes are updated via enrollment (i.e. OAuth), the partner
    must send ``ENROLLMENT``. When scopes are updated in a post-enrollment view, the partner must send ``PORTAL``."""


class ItemApplicationScopesUpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    application_id: str
    scopes: Scopes | ScopesDict
    state: NotRequired[str]
    context: ScopesContextOrStr
