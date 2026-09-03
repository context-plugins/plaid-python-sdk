from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .enums.consumer_report_category import ConsumerReportCategoryOrStr


class ConsumerDispute(SdkBaseModel):
    """The information about a previously submitted valid dispute statement by the consumer"""

    consumer_dispute_id: str
    """(Deprecated) A unique identifier (UUID) of the consumer dispute that can be used for troubleshooting"""

    dispute_field_create_date: Date
    """Date of the disputed field (e.g. transaction date), in an ISO 8601 format (YYYY-MM-DD)"""

    category: ConsumerReportCategoryOrStr
    """Type of data being disputed by the consumer"""

    statement: str
    """Text content of dispute"""


class ConsumerDisputeDict(TypedDict):
    consumer_dispute_id: str
    dispute_field_create_date: Date
    category: ConsumerReportCategoryOrStr
    statement: str
