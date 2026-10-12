from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .jwkpublic_key import JwkpublicKey, JwkpublicKeyDict


class WebhookVerificationKeyGetResponse(SdkBaseModel):
    """WebhookVerificationKeyGetResponse defines the response schema for ``/webhook_verification_key/get``"""

    key: JwkpublicKey
    """A JSON Web Key (JWK) that can be used in conjunction with `JWT libraries <https://jwt.io/#libraries-io>`__ to
    verify Plaid webhooks"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WebhookVerificationKeyGetResponseDict(TypedDict):
    key: JwkpublicKeyDict
    request_id: str
