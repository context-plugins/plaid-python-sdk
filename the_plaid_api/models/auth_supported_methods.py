from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthSupportedMethods(SdkBaseModel):
    """Metadata specifically related to which auth methods an institution supports."""

    instant_auth: bool
    """Indicates if instant auth is supported."""

    instant_match: bool
    """Indicates if instant match is supported."""

    automated_micro_deposits: bool
    """Indicates if automated micro-deposits are supported."""

    instant_micro_deposits: bool
    """Indicates if instant micro-deposits are supported."""


class AuthSupportedMethodsDict(TypedDict):
    instant_auth: bool
    instant_match: bool
    automated_micro_deposits: bool
    instant_micro_deposits: bool
