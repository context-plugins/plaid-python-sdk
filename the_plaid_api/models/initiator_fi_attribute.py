from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InitiatorFiAttribute(SdkBaseModel):
    """Initiator Fi Attribute"""

    name: Optional[str] = UNSET
    value: Optional[str] = UNSET


class InitiatorFiAttributeDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
