from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class JwkpublicKey(SdkBaseModel):
    """A JSON Web Key (JWK) that can be used in conjunction with `JWT libraries <https://jwt.io/#libraries-io>`__ to
    verify Plaid webhooks"""

    alg: str
    """The alg member identifies the cryptographic algorithm family used with the key."""

    crv: str
    """The crv member identifies the cryptographic curve used with the key."""

    kid: str
    """The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a
    set of keys within the JWK during key rollover."""

    kty: str
    """The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or
    EC."""

    use: str
    """The use (public key use) parameter identifies the intended use of the public key."""

    x: str
    """The x member contains the x coordinate for the elliptic curve point, provided as a base64url-encoded string of
    the coordinate's big endian representation."""

    y: str
    """The y member contains the y coordinate for the elliptic curve point, provided as a base64url-encoded string of
    the coordinate's big endian representation."""

    created_at: int
    """The timestamp when the key was created, in Unix time."""

    expired_at: int | None
    """The timestamp when the key expired, in Unix time."""


class JwkpublicKeyDict(TypedDict):
    alg: str
    crv: str
    kid: str
    kty: str
    use: str
    x: str
    y: str
    created_at: int
    expired_at: int | None
