from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReasonCode(str, Enum):
    """Specifies the reason for cancelling transfer. This is required for RfP transfers, and will be ignored for other
    networks.

    ``"AC03"`` - Invalid Creditor Account Number

    ``"AM09"`` - Incorrect Amount

    ``"CUST"`` - Requested By Customer - Cancellation requested

    ``"DUPL"`` - Duplicate Payment

    ``"FRAD"`` - Fraudulent Payment - Unauthorized or fraudulently induced

    ``"TECH"`` - Technical Problem - Cancellation due to system issues

    ``"UPAY"`` - Undue Payment - Payment was made through another channel

    ``"AC14"`` - Invalid or Missing Creditor Account Type

    ``"AM06"`` - Amount Too Low

    ``"BE05"`` - Unrecognized Initiating Party

    ``"FOCR"`` - Following Refund Request

    ``"MS02"`` - No Specified Reason - Customer

    ``"MS03"`` - No Specified Reason - Agent

    ``"RR04"`` - Regulatory Reason

    ``"RUTA"`` - Return Upon Unable To Apply"""

    AC03 = "AC03"
    AM09 = "AM09"
    CUST = "CUST"
    DUPL = "DUPL"
    FRAD = "FRAD"
    TECH = "TECH"
    UPAY = "UPAY"
    AC14 = "AC14"
    AM06 = "AM06"
    BE05 = "BE05"
    FOCR = "FOCR"
    MS02 = "MS02"
    MS03 = "MS03"
    RR04 = "RR04"
    RUTA = "RUTA"

    __str__ = str.__str__


ReasonCodeOrStr: TypeAlias = Annotated[ReasonCode | str, open_enum_validator(ReasonCode)]
