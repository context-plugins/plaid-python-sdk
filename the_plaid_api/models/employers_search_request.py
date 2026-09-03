from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EmployersSearchRequest(SdkBaseModel):
    """EmployersSearchRequest defines the request schema for ``/employers/search``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    query: str
    """The employer name to be searched for."""

    products: list[str]
    """The Plaid products the returned employers should support. Currently, this field must be set to
    ``"deposit_switch"``."""


class EmployersSearchRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    query: str
    products: list[str]
