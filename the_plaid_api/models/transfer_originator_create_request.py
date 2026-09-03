from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferOriginatorCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/originator/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    company_name: str
    """The company name of the end customer being created. This will be displayed in public-facing surfaces, e.g. Plaid
    Dashboard."""


class TransferOriginatorCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    company_name: str
