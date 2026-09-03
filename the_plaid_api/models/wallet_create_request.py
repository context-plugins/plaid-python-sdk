from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.iso_currency_code import IsoCurrencyCodeOrStr


class WalletCreateRequest(SdkBaseModel):
    """WalletCreateRequest defines the request schema for ``/wallet/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    iso_currency_code: IsoCurrencyCodeOrStr
    """An ISO-4217 currency code, used with e-wallets and transactions."""


class WalletCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    iso_currency_code: IsoCurrencyCodeOrStr
