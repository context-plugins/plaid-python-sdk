from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.oauth_grant_type import OauthGrantTypeOrStr
from .enums.oauth_subject_token_type import OauthSubjectTokenTypeOrStr


class OauthTokenRequest(SdkBaseModel):
    """OAuth token grant request."""

    grant_type: OauthGrantTypeOrStr
    """The type of OAuth grant being requested:

    ``client_credentials`` allows exchanging a client id and client secret for a refresh and access token.
    ``refresh_token`` allows refreshing an access token using a refresh token. When using this grant type, only the
    ``refresh_token`` field is required (along with the ``client_id`` and ``client_secret``).
    ``urn:ietf:params:oauth:grant-type:token-exchange`` allows exchanging a subject token for an OAuth token. When using
    this grant type, the ``audience``, ``subject_token`` and ``subject_token_type`` fields are required. These grants
    are defined in their respective RFCs. ``refresh_token`` and ``client_credentials`` are defined in RFC 6749 and
    ``urn:ietf:params:oauth:grant-type:token-exchange`` is defined in RFC 8693."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    client_secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body as either ``secret`` or ``client_secret``."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body as either ``secret`` or ``client_secret``."""

    scope: Optional[str] = UNSET
    """A space-separated list of scopes associated with this token, in the format described in
    https://datatracker.ietf.org/doc/html/rfc6749#section-3.3. Currently accepted values are:

    ``user:read`` allows reading user data. ``user:write`` allows writing user data. ``exchange`` allows exchanging a
    token using the ``urn:plaid:params:oauth:user-token`` subject token type. ``mcp:dashboard`` allows access to the MCP
    dashboard server."""

    refresh_token: Optional[str] = UNSET
    """Refresh token for OAuth"""

    resource: Optional[str] = UNSET
    """URI of the target resource server"""

    audience: Optional[str] = UNSET
    """Used when exchanging a token. The meaning depends on the ``subject_token_type``:

    - For ``urn:plaid:params:tokens:user``: Must be the same as the ``client_id``.
    - For ``urn:plaid:params:oauth:user-token``: The other ``client_id`` to exchange tokens to.
    - For ``urn:plaid:params:credit:multi-user``: a ``client_id`` or one of the supported CRA partner URNs:
        ``urn:plaid:params:cra-partner:experian``, ``urn:plaid:params:cra-partner:fannie-mae``, or
        ``urn:plaid:params:cra-partner:freddie-mac``."""

    subject_token: Optional[str] = UNSET
    """Token representing the subject. The meaning depends on the ``subject_token_type``. For
    ``urn:plaid:params:tokens:user``, the ``subject_token`` must be a Plaid-issued user token from the ``/user/create``
    endpoint. For ``urn:plaid:params:oauth:user-token``, the ``subject_token`` must be an OAuth refresh token issued
    from the ``/oauth/token`` endpoint."""

    subject_token_type: Optional[OauthSubjectTokenTypeOrStr] = UNSET
    """The type of the subject token. ``urn:plaid:params:tokens:user`` allows exchanging a Plaid-issued user token for
    an OAuth token. When using this token type, ``audience`` must be the same as the ``client_id``. ``subject_token``
    must be a Plaid-issued user token issued from the ``/user/create`` endpoint. ``urn:plaid:params:oauth:user-token``
    allows exchanging a refresh token for an OAuth token to another ``client_id``. The other ``client_id`` is provided
    in ``audience``. ``subject_token`` must be an OAuth refresh token issued from the ``/oauth/token`` endpoint.
    ``urn:plaid:params:credit:multi-user`` allows exchanging a Plaid-issued user token for an OAuth token. When using
    this token type, ``audience`` may be a client id or a supported CRA partner URN. ``audience`` supports a
    comma-delimited list of clients. When multiple clients are specified in the ``audience`` a multi-party token is
    created which can be used by all parties in the audience in conjunction with their ``client_id`` and
    ``client_secret``."""


class OauthTokenRequestDict(TypedDict):
    grant_type: OauthGrantTypeOrStr
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    secret: NotRequired[str]
    scope: NotRequired[str]
    refresh_token: NotRequired[str]
    resource: NotRequired[str]
    audience: NotRequired[str]
    subject_token: NotRequired[str]
    subject_token_type: NotRequired[OauthSubjectTokenTypeOrStr]
