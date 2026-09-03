from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AssetReportGetRequestOptions(SdkBaseModel):
    """An optional object to filter or add data to ``/asset_report/get`` results. If provided, must be non-``null``."""

    days_to_include: OptionalNullable[int] = UNSET
    """The maximum number of days of history to include in the Asset Report."""


class AssetReportGetRequestOptionsDict(TypedDict):
    days_to_include: NotRequired[int | None]
