from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Category(SdkBaseModel):
    """Information describing a transaction category"""

    category_id: str
    """An identifying number for the category. ``category_id`` is a Plaid-specific identifier and does not necessarily
    correspond to merchant category codes."""

    group: str
    """``place`` for physical transactions or ``special`` for other transactions such as bank charges."""

    hierarchy: list[str]
    """A hierarchical array of the categories to which this ``category_id`` belongs."""


class CategoryDict(TypedDict):
    category_id: str
    group: str
    hierarchy: list[str]
