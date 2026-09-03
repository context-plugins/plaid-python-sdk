from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.image_quality_outcome import ImageQualityOutcomeOrStr


class ImageQualityDetails(SdkBaseModel):
    """Details about the image quality of the document."""

    glare_check: ImageQualityOutcomeOrStr
    """The outcome of the glare check.

    ``success`` - The image is free of glare.

    ``failed`` - The image contains glare that may obscure document details."""

    dimensions_check: ImageQualityOutcomeOrStr
    """The outcome of the dimensions check.

    ``success`` - The image meets the minimum size and resolution requirements.

    ``failed`` - The image does not meet the minimum size or resolution requirements."""

    blur_check: ImageQualityOutcomeOrStr
    """The outcome of the blur check.

    ``success`` - The image is sufficiently sharp.

    ``failed`` - The image is too blurry for analysis."""


class ImageQualityDetailsDict(TypedDict):
    glare_check: ImageQualityOutcomeOrStr
    dimensions_check: ImageQualityOutcomeOrStr
    blur_check: ImageQualityOutcomeOrStr
