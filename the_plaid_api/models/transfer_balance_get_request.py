from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.transfer_balance_type import TransferBalanceTypeOrStr


class TransferBalanceGetRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/balance/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Client ID of the end customer."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    type_: Optional[TransferBalanceTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of balance.

    ``prefunded_rtp_credits`` - Your prefunded RTP credit balance with Plaid ``prefunded_ach_credits`` - Your prefunded
    ACH credit balance with Plaid"""


class TransferBalanceGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    originator_client_id: NotRequired[str | None]
    secret: NotRequired[str]
    type_: NotRequired[TransferBalanceTypeOrStr]
