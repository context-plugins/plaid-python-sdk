from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ApplicationGetRequest(SdkBaseModel):
    """ApplicationGetRequest defines the schema for ``/application/get``"""

    client_id: str
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: str
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    application_id: str
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""


class ApplicationGetRequestDict(TypedDict):
    client_id: str
    secret: str
    application_id: str
