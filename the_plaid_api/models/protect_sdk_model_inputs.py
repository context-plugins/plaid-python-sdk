from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProtectSdkModelInputs(SdkBaseModel):
    """Inputs for Protect SDK Trust Index models."""

    sdk_session_id: str
    """A unique identifier for the Protect SDK session, used to compute a Trust Index score and fraud attributes."""


class ProtectSdkModelInputsDict(TypedDict):
    sdk_session_id: str
