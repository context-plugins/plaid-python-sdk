from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdentityVerificationTemplateReference(SdkBaseModel):
    """The resource ID and version number of the template configuring the behavior of a given Identity Verification."""

    id: str
    """ID of the associated Identity Verification template. Like all Plaid identifiers, this is case-sensitive."""

    version: int
    """Version of the associated Identity Verification template."""


class IdentityVerificationTemplateReferenceDict(TypedDict):
    id: str
    version: int
