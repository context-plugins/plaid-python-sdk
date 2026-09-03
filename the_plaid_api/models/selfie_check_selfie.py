from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.selfie_status import SelfieStatusOrStr
from .selfie_analysis import SelfieAnalysis, SelfieAnalysisDict
from .selfie_capture import SelfieCapture, SelfieCaptureDict


class SelfieCheckSelfie(SdkBaseModel):
    """Captures and analysis from a user's selfie."""

    status: SelfieStatusOrStr
    """An outcome status for this specific selfie. Distinct from the overall ``selfie_check.status`` that summarizes the
    verification outcome from one or more selfies."""

    attempt: int
    """The ``attempt`` field begins with 1 and increments with each subsequent selfie upload."""

    capture: SelfieCapture
    """The image or video capture of a selfie. Only one of ``image_url`` or ``video_url`` will be populated per selfie.
    In the vast majority of sessions Plaid records a short video of the user, so ``video_url`` is populated and
    ``image_url`` is ``null``. ``image_url`` is only populated in the rare passive-liveness fallback case, where the
    user's device could not complete the standard video liveness capture (for example, a camera or streaming error) and
    submitted a single still image instead."""

    analysis: SelfieAnalysis
    """High level descriptions of how the associated selfie was processed. If a selfie fails verification, the details
    in the ``analysis`` object should help clarify why the selfie was rejected."""


class SelfieCheckSelfieDict(TypedDict):
    status: SelfieStatusOrStr
    attempt: int
    capture: SelfieCapture | SelfieCaptureDict
    analysis: SelfieAnalysis | SelfieAnalysisDict
