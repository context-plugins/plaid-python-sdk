from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_verification_income_account import CraVerificationIncomeAccount, CraVerificationIncomeAccountDict


class CraVerificationIncomeItem(SdkBaseModel):
    """The details and metadata for an end user's Item within the Home Lending Income Report."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    accounts: list[CraVerificationIncomeAccount]
    """The Item's accounts that have bank income data."""

    last_updated_time: RFC3339DateTime
    """The time when this Item's data was last retrieved from the financial institution."""

    institution_id: str
    """The unique identifier of the institution associated with the Item."""

    institution_name: str
    """The name of the institution associated with the Item."""


class CraVerificationIncomeItemDict(TypedDict):
    item_id: str
    accounts: list[CraVerificationIncomeAccount | CraVerificationIncomeAccountDict]
    last_updated_time: RFC3339DateTime
    institution_id: str
    institution_name: str
