from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxItemApplicationSeedRequest(SdkBaseModel):
    """SandboxItemApplicationSeedRequest defines the request schema for ``/sandbox/item/application/seed``"""

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


class SandboxItemApplicationSeedRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    application_id: str
