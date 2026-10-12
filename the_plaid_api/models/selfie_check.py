from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.selfie_check_status import SelfieCheckStatusOrStr
from .selfie_check_selfie import SelfieCheckSelfie, SelfieCheckSelfieDict


class SelfieCheck(SdkBaseModel):
    """Additional information for the ``selfie_check`` step. This field will be ``null`` unless ``steps.selfie_check``
    has reached a terminal state of either ``success`` or ``failed``."""

    status: SelfieCheckStatusOrStr
    """The outcome status for the associated Identity Verification attempt's ``selfie_check`` step. This field will
    always have the same value as ``steps.selfie_check``."""

    selfies: list[SelfieCheckSelfie]
    """An array of selfies submitted to the ``selfie_check`` step. Each entry represents one user submission."""


class SelfieCheckDict(TypedDict):
    status: SelfieCheckStatusOrStr
    selfies: list[SelfieCheckSelfieDict]
