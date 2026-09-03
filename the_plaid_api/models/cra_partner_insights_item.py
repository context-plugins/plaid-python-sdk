from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_partner_insights_item_account import CraPartnerInsightsItemAccount, CraPartnerInsightsItemAccountDict


class CraPartnerInsightsItem(SdkBaseModel):
    """The details and metadata for an end user's Item."""

    institution_id: Optional[str] = UNSET
    """The ID for the institution that the user linked."""

    institution_name: Optional[str] = UNSET
    """The name of the institution the user linked."""

    item_id: Optional[str] = UNSET
    """The identifier for the Item."""

    accounts: Optional[list[CraPartnerInsightsItemAccount]] = UNSET
    """A list of accounts in the Item."""


class CraPartnerInsightsItemDict(TypedDict):
    institution_id: NotRequired[str]
    institution_name: NotRequired[str]
    item_id: NotRequired[str]
    accounts: NotRequired[list[CraPartnerInsightsItemAccount | CraPartnerInsightsItemAccountDict]]
