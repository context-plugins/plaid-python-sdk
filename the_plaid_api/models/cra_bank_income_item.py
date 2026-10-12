from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .cra_bank_income_account import CraBankIncomeAccount, CraBankIncomeAccountDict
from .cra_bank_income_source import CraBankIncomeSource, CraBankIncomeSourceDict


class CraBankIncomeItem(SdkBaseModel):
    """The details and metadata for an end user's Item."""

    item_id: Optional[str] = UNSET
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    accounts: Optional[list[CraBankIncomeAccount]] = UNSET
    """The Item's accounts that have bank income data."""

    bank_income_accounts: list[CraBankIncomeAccount]
    """This is a V1 (II1) field. For the V2 (II2) equivalent, use the ``accounts`` field. The Item's accounts that have
    bank income data."""

    bank_income_sources: list[CraBankIncomeSource]
    """This is a V1 (II1) field. For the V2 (II2) equivalent, use the report-level ``income_streams`` field. The income
    sources for this Item. Each entry in the array is a single income source."""

    last_updated_time: Optional[RFC3339DateTime] = UNSET
    """The time when this Item's data was last retrieved from the financial institution."""

    institution_id: Optional[str] = UNSET
    """The unique identifier of the institution associated with the Item."""

    institution_name: Optional[str] = UNSET
    """The name of the institution associated with the Item."""


class CraBankIncomeItemDict(TypedDict):
    item_id: NotRequired[str]
    accounts: NotRequired[list[CraBankIncomeAccountDict]]
    bank_income_accounts: list[CraBankIncomeAccountDict]
    bank_income_sources: list[CraBankIncomeSourceDict]
    last_updated_time: NotRequired[RFC3339DateTime]
    institution_id: NotRequired[str]
    institution_name: NotRequired[str]
