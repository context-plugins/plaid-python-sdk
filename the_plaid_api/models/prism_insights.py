from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrismInsights(SdkBaseModel):
    """The data from the Insights product returned by Prism Data."""

    version: int
    """The version of Prism Data's insights model used. This field is deprecated in favor of ``model_version``."""

    model_version: Optional[str] = UNSET
    """The version of Prism Data's insights model used."""

    result: Optional[Any] = UNSET
    """The Insights Result object is a map of cash flow attributes, where the key is a string, and the value is a float
    or string. For a full list of attributes, contact your account manager. The attributes may vary depending on the
    Prism version used."""

    error_reason: Optional[str] = UNSET
    """The error returned by Prism for this product."""


class PrismInsightsDict(TypedDict):
    version: int
    model_version: NotRequired[str]
    result: NotRequired[Any]
    error_reason: NotRequired[str]
