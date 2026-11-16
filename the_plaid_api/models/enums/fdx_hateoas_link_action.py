from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxHateoasLinkAction(str, Enum):
    """HTTP Method to use for the request"""

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"
    PUT = "PUT"

    __str__ = str.__str__


FdxHateoasLinkActionOrStr: TypeAlias = Annotated[FdxHateoasLinkAction | str, open_enum_validator(FdxHateoasLinkAction)]
