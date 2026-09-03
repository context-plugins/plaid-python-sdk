from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .payroll_income_account_data import PayrollIncomeAccountData, PayrollIncomeAccountDataDict
from .payroll_income_object import PayrollIncomeObject, PayrollIncomeObjectDict
from .payroll_item_status import PayrollItemStatus, PayrollItemStatusDict


class PayrollItem(SdkBaseModel):
    """An object containing information about the payroll item."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    institution_id: str
    """The unique identifier of the institution associated with the Item."""

    institution_name: str
    """The name of the institution associated with the Item."""

    accounts: list[PayrollIncomeAccountData]
    payroll_income: list[PayrollIncomeObject]
    status: PayrollItemStatus | None
    """Details about the status of the payroll item."""

    updated_at: RFC3339DateTime | None
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDTHH:mm:ssZ) indicating the last
    time that the Item was updated."""


class PayrollItemDict(TypedDict):
    item_id: str
    institution_id: str
    institution_name: str
    accounts: list[PayrollIncomeAccountData | PayrollIncomeAccountDataDict]
    payroll_income: list[PayrollIncomeObject | PayrollIncomeObjectDict]
    status: PayrollItemStatus | PayrollItemStatusDict | None
    updated_at: RFC3339DateTime | None
