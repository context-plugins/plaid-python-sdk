from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenEuconfig(SdkBaseModel):
    """Configuration parameters for EU flows"""

    headless: Optional[bool] = UNSET
    """If ``true``, open Link without an initial UI. Defaults to ``false``."""


class LinkTokenEuconfigDict(TypedDict):
    headless: NotRequired[bool]
