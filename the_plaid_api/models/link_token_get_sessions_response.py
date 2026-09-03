from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .link_event import LinkEvent, LinkEventDict
from .link_session_exit import LinkSessionExit, LinkSessionExitDict
from .link_session_exit_deprecated import LinkSessionExitDeprecated, LinkSessionExitDeprecatedDict
from .link_session_results import LinkSessionResults, LinkSessionResultsDict
from .link_session_success import LinkSessionSuccess, LinkSessionSuccessDict


class LinkTokenGetSessionsResponse(SdkBaseModel):
    """An object containing information about a link session. Session data will be provided for up to six hours after
    the session has ended."""

    link_session_id: str
    """The unique ID for the link session."""

    started_at: Optional[RFC3339DateTime] = UNSET
    """The timestamp at which the link session was first started, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format."""

    finished_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp at which the link session was finished, if available, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    on_success: OptionalNullable[LinkSessionSuccess] = UNSET
    """An object representing an `onSuccess <https://plaid.com/docs/link/web/#onsuccess>`__ callback from Link. This
    field is returned only for legacy integrations and is deprecated in favor of
    https://plaid.com/docs/api/link/#link-token-get-response-link-sessions-results-item-add-results which can support
    multiple public tokens in a single Link session, for flows such as multi-Item Link. If you are receiving
    ``on_success``, contact your account manager to migrate to ``results.item_add_results`` instead."""

    on_exit: OptionalNullable[LinkSessionExitDeprecated] = UNSET
    """An object representing an `onExit <https://plaid.com/docs/link/web/#onexit>`__ callback from Link. This field is
    returned only for legacy implementations and has been deprecated in favor of
    https://plaid.com/docs/api/link/#link-token-get-response-link-sessions-exit, for improved naming consistency. If you
    are receiving this field, contact your account manager to migrate to the newer ``exit`` field."""

    exit: OptionalNullable[LinkSessionExit] = UNSET
    """An object representing an `onExit <https://plaid.com/docs/link/web/#onexit>`__ callback from Link. If you are not
    receiving this field and are instead receiving the deprecated ``on_exit`` field, contact your account manager to
    update your integration."""

    events: Optional[list[LinkEvent]] = UNSET
    """List of customer-related Link events"""

    results: OptionalNullable[LinkSessionResults] = UNSET
    """The set of results for a Link session."""


class LinkTokenGetSessionsResponseDict(TypedDict):
    link_session_id: str
    started_at: NotRequired[RFC3339DateTime]
    finished_at: NotRequired[RFC3339DateTime | None]
    on_success: NotRequired[LinkSessionSuccess | LinkSessionSuccessDict | None]
    on_exit: NotRequired[LinkSessionExitDeprecated | LinkSessionExitDeprecatedDict | None]
    exit: NotRequired[LinkSessionExit | LinkSessionExitDict | None]
    events: NotRequired[list[LinkEvent | LinkEventDict]]
    results: NotRequired[LinkSessionResults | LinkSessionResultsDict | None]
