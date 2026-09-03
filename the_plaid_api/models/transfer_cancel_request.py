from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.reason_code import ReasonCodeOrStr


class TransferCancelRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/cancel``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: str
    """Plaid's unique identifier for a transfer."""

    originator_client_id: OptionalNullable[str] = UNSET
    """The Plaid client ID of the transfer originator. Should only be present if ``client_id`` is a third-party sender
    (TPS)."""

    reason_code: Optional[ReasonCodeOrStr] = UNSET
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


class TransferCancelRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: str
    originator_client_id: NotRequired[str | None]
    reason_code: NotRequired[ReasonCodeOrStr]
