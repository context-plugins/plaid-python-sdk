from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FiAttributeEntity(SdkBaseModel):
    """Financial Institution provider-specific attribute"""

    name: str
    """Name of attribute"""

    value: str
    """Value of attribute"""


class FiAttributeEntityDict(TypedDict):
    name: str
    value: str
