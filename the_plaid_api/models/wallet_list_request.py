from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.iso_currency_code import IsoCurrencyCodeOrStr


class WalletListRequest(SdkBaseModel):
    """WalletListRequest defines the request schema for ``/wallet/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    iso_currency_code: Optional[IsoCurrencyCodeOrStr] = UNSET
    """An ISO-4217 currency code, used with e-wallets and transactions."""

    cursor: Optional[str] = UNSET
    """A base64 value representing the latest e-wallet that has already been requested. Set this to ``next_cursor``
    received from the previous ``/wallet/list`` request. If provided, the response will only contain e-wallets created
    before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in
    descending order."""

    count: int = 10
    """The number of e-wallets to fetch"""


class WalletListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    iso_currency_code: NotRequired[IsoCurrencyCodeOrStr]
    cursor: NotRequired[str]
    count: NotRequired[int]
