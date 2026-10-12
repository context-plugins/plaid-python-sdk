from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .total_report_inflow_amount import TotalReportInflowAmount, TotalReportInflowAmountDict
from .total_report_outflow_amount import TotalReportOutflowAmount, TotalReportOutflowAmountDict


class CraVoaReportAttributes(SdkBaseModel):
    """Attributes for the VOA report."""

    total_inflow_amount: TotalReportInflowAmount | None
    """Total amount of debit transactions into the report's accounts in the time period of the report. This field only
    takes into account USD transactions from the accounts."""

    total_outflow_amount: TotalReportOutflowAmount | None
    """Total amount of credit transactions out of the report's accounts in the time period of the report. This field
    only takes into account USD transactions from the accounts."""


class CraVoaReportAttributesDict(TypedDict):
    total_inflow_amount: TotalReportInflowAmountDict | None
    total_outflow_amount: TotalReportOutflowAmountDict | None
