from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenEuConfig(SdkBaseModel):
    """Configuration parameters for EU flows"""

    headless: Optional[bool] = UNSET
    """If ``true``, open Link without an initial UI. Defaults to ``false``."""


class LinkTokenEuConfigDict(TypedDict):
    headless: NotRequired[bool]
