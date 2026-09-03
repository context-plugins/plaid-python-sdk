from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ImageQuality(str, Enum):
    """A high level description of the quality of the image the user submitted.

    For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be
    marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.

    Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we
    attribute the failure to low image quality."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    __str__ = str.__str__


ImageQualityOrStr: TypeAlias = Annotated[ImageQuality | str, open_enum_validator(ImageQuality)]
