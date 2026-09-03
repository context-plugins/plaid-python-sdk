from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict
from .link_session_exit_metadata import LinkSessionExitMetadata, LinkSessionExitMetadataDict


class LinkSessionExitDeprecated(SdkBaseModel):
    """An object representing an `onExit <https://plaid.com/docs/link/web/#onexit>`__ callback from Link. This field is
    returned only for legacy implementations and has been deprecated in favor of
    https://plaid.com/docs/api/link/#link-token-get-response-link-sessions-exit, for improved naming consistency. If you
    are receiving this field, contact your account manager to migrate to the newer ``exit`` field."""

    error: Error | None
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    metadata: LinkSessionExitMetadata | None
    """Displayed if a user exits Link without successfully linking an Item."""


class LinkSessionExitDeprecatedDict(TypedDict):
    error: Error | ErrorDict | None
    metadata: LinkSessionExitMetadata | LinkSessionExitMetadataDict | None
