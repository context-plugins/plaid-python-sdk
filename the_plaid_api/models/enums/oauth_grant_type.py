from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OauthGrantType(str, Enum):
    """The type of OAuth grant being requested:

    ``client_credentials`` allows exchanging a client id and client secret for a refresh and access token.
    ``refresh_token`` allows refreshing an access token using a refresh token. When using this grant type, only the
    ``refresh_token`` field is required (along with the ``client_id`` and ``client_secret``).
    ``urn:ietf:params:oauth:grant-type:token-exchange`` allows exchanging a subject token for an OAuth token. When using
    this grant type, the ``audience``, ``subject_token`` and ``subject_token_type`` fields are required. These grants
    are defined in their respective RFCs. ``refresh_token`` and ``client_credentials`` are defined in RFC 6749 and
    ``urn:ietf:params:oauth:grant-type:token-exchange`` is defined in RFC 8693."""

    REFRESH_TOKEN = "refresh_token"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"
    CLIENT_CREDENTIALS = "client_credentials"

    __str__ = str.__str__


OauthGrantTypeOrStr: TypeAlias = Annotated[OauthGrantType | str, open_enum_validator(OauthGrantType)]
