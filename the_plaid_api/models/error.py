from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.plaid_error_type import PlaidErrorTypeOrStr


class Error(SdkBaseModel):
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    error_type: PlaidErrorTypeOrStr
    """A broad categorization of the error. Safe for programmatic use."""

    error_code: str
    """The particular error code. Safe for programmatic use."""

    error_code_reason: OptionalNullable[str] = UNSET
    """The specific reason for the error code. Currently, reasons are only supported for OAuth-based item errors;
    ``null`` will be returned otherwise. Safe for programmatic use.

    Possible values: ``OAUTH_INVALID_TOKEN``: The user's OAuth connection to this institution has been invalidated.

    ``OAUTH_CONSENT_EXPIRED``: The user's access consent for this OAuth connection to this institution has expired.

    ``OAUTH_USER_REVOKED``: The user's OAuth connection to this institution is invalid because the user revoked their
    connection."""

    error_message: str
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic
    use."""

    display_message: str | None
    """A user-friendly representation of the error code. ``null`` if the error is not related to user action.

    This may change over time and is not safe for programmatic use."""

    request_id: Optional[str] = UNSET
    """A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in
    errors provided by webhooks."""

    causes: Optional[list[Any]] = UNSET
    """In this product, a request can pertain to more than one Item. If an error is returned for such a request,
    ``causes`` will return an array of errors containing a breakdown of these errors on the individual Item level, if
    any can be identified.

    ``causes`` will be provided for the ``error_type`` ``ASSET_REPORT_ERROR`` or ``CHECK_REPORT_ERROR``. ``causes`` will
    also not be populated inside an error nested within a ``warning`` object."""

    status: OptionalNullable[int] = UNSET
    """The HTTP status code associated with the error. This will only be returned in the response body when the error
    information is provided via a webhook."""

    documentation_url: Optional[str] = UNSET
    """The URL of a Plaid documentation page with more information about the error"""

    suggested_action: OptionalNullable[str] = UNSET
    """Suggested steps for resolving the error"""

    required_account_subtypes: Optional[list[str]] = UNSET
    """A list of the account subtypes that were requested via the ``account_filters`` parameter in
    ``/link/token/create``. Currently only populated for ``NO_ACCOUNTS`` errors from Items with ``investments_auth`` as
    an enabled product."""

    provided_account_subtypes: Optional[list[str]] = UNSET
    """A list of the account subtypes that were extracted but did not match the requested subtypes via the
    ``account_filters`` parameter in ``/link/token/create``. Currently only populated for ``NO_ACCOUNTS`` errors from
    Items with ``investments_auth`` as an enabled product."""


class ErrorDict(TypedDict):
    error_type: PlaidErrorTypeOrStr
    error_code: str
    error_code_reason: NotRequired[str | None]
    error_message: str
    display_message: str | None
    request_id: NotRequired[str]
    causes: NotRequired[list[Any]]
    status: NotRequired[int | None]
    documentation_url: NotRequired[str]
    suggested_action: NotRequired[str | None]
    required_account_subtypes: NotRequired[list[str]]
    provided_account_subtypes: NotRequired[list[str]]
