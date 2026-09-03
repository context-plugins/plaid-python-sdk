from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cause import Cause, CauseDict
from .enums.base_report_warning_code import BaseReportWarningCodeOrStr


class BaseReportWarning(SdkBaseModel):
    """It is possible for a Base Report to be returned with missing account owner information. In such cases, the Base
    Report will contain warning data in the response, indicating why obtaining the owner information failed."""

    warning_type: str
    """The warning type, which will always be ``BASE_REPORT_WARNING``"""

    warning_code: BaseReportWarningCodeOrStr
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Account-owner information is
    not available. ``TRANSACTIONS_UNAVAILABLE``: Transactions information associated with Credit and Depository accounts
    are unavailable. ``USER_FRAUD_ALERT``: The User has placed a fraud alert on their Plaid Check consumer report due to
    suspected fraud. Note: when a fraud alert is in place, the recipient of the consumer report has an obligation to
    verify the consumer's identity."""

    cause: Cause | None
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""


class BaseReportWarningDict(TypedDict):
    warning_type: str
    warning_code: BaseReportWarningCodeOrStr
    cause: Cause | CauseDict | None
