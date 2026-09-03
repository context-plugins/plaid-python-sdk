from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OauthSubjectTokenType(str, Enum):
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

    URN_PLAID_PARAMS_TOKENS_USER = "urn:plaid:params:tokens:user"
    URN_PLAID_PARAMS_OAUTH_USER_TOKEN = "urn:plaid:params:oauth:user-token"
    URN_PLAID_PARAMS_CREDIT_MULTI_USER = "urn:plaid:params:credit:multi-user"

    __str__ = str.__str__


OauthSubjectTokenTypeOrStr: TypeAlias = Annotated[
    OauthSubjectTokenType | str, open_enum_validator(OauthSubjectTokenType)
]
