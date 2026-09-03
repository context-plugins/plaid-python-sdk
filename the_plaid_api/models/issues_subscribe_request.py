from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IssuesSubscribeRequest(SdkBaseModel):
    """IssuesSubscribeRequest defines the request schema for ``/issues/subscribe``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    issue_id: str
    """The unique identifier of the issue to subscribe to."""

    webhook: str
    """The webhook URL where notifications should be sent when the issue status changes."""


class IssuesSubscribeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    issue_id: str
    webhook: str
