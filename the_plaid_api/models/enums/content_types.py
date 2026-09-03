from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentTypes(str, Enum):
    """Types of document formats. (Suggested values)"""

    APPLICATION_PDF = "application/pdf"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_TIFF = "image/tiff"
    IMAGE_PNG = "image/png"
    APPLICATION_JSON = "application/json"

    __str__ = str.__str__


ContentTypesOrStr: TypeAlias = Annotated[ContentTypes | str, open_enum_validator(ContentTypes)]
