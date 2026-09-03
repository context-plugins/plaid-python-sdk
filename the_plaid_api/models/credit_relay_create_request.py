from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CreditRelayCreateRequest(SdkBaseModel):
    """CreditRelayCreateRequest defines the request schema for ``/credit/relay/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    report_tokens: list[str]
    """List of report token strings, with at most one token of each report type. Currently only Asset Report token is
    supported."""

    secondary_client_id: str
    """The ``secondary_client_id`` is the client id of the third party with whom you would like to share the relay
    token."""

    webhook: OptionalNullable[str] = UNSET
    """URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling
    ``/credit/relay/get``."""


class CreditRelayCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    report_tokens: list[str]
    secondary_client_id: str
    webhook: NotRequired[str | None]
