from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_voa_report_account import CraVoaReportAccount, CraVoaReportAccountDict


class CraVoaReportItem(SdkBaseModel):
    """A representation of an Item within a VOA report."""

    accounts: list[CraVoaReportAccount]
    """Data about each of the accounts open on the Item."""

    institution_name: str
    """The full financial institution name associated with the Item."""

    institution_id: str
    """The id of the financial institution associated with the Item."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    last_update_time: RFC3339DateTime
    """The date and time when this Item's data was last retrieved from the financial institution, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format."""


class CraVoaReportItemDict(TypedDict):
    accounts: list[CraVoaReportAccount | CraVoaReportAccountDict]
    institution_name: str
    institution_id: str
    item_id: str
    last_update_time: RFC3339DateTime
