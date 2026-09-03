from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .auth_supported_methods import AuthSupportedMethods, AuthSupportedMethodsDict


class AuthMetadata(SdkBaseModel):
    """Metadata that captures information about the Auth features of an institution."""

    supported_methods: AuthSupportedMethods | None
    """Metadata specifically related to which auth methods an institution supports."""


class AuthMetadataDict(TypedDict):
    supported_methods: AuthSupportedMethods | AuthSupportedMethodsDict | None
