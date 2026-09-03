from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxFdxConsentSeedResponse(SdkBaseModel):
    """Response containing the identifier of the seeded FDX consent grant, which can then be listed, retrieved, and
    revoked through the FDX Consent API."""

    consent_id: str
    """The identifier of the newly seeded FDX consent grant."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxFdxConsentSeedResponseDict(TypedDict):
    consent_id: str
    request_id: str
