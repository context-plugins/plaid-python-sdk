from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraNetworkInsightsItem(SdkBaseModel):
    """Contains data about the connected Item."""

    institution_id: str
    """The ID for the institution the user linked."""

    institution_name: str
    """The name of the institution the user linked."""

    item_id: str
    """The identifier for the Item."""


class CraNetworkInsightsItemDict(TypedDict):
    institution_id: str
    institution_name: str
    item_id: str
