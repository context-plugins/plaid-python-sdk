from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link_session_success_metadata import LinkSessionSuccessMetadata, LinkSessionSuccessMetadataDict


class LinkSessionSuccess(SdkBaseModel):
    """An object representing an `onSuccess <https://plaid.com/docs/link/web/#onsuccess>`__ callback from Link. This
    field is returned only for legacy integrations and is deprecated in favor of
    https://plaid.com/docs/api/link/#link-token-get-response-link-sessions-results-item-add-results which can support
    multiple public tokens in a single Link session, for flows such as multi-Item Link. If you are receiving
    ``on_success``, contact your account manager to migrate to ``results.item_add_results`` instead."""

    public_token: str
    """Displayed once a user has successfully linked their Item."""

    metadata: LinkSessionSuccessMetadata | None
    """Displayed once a user has successfully linked their Item."""


class LinkSessionSuccessDict(TypedDict):
    public_token: str
    metadata: LinkSessionSuccessMetadataDict | None
