from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BankTransferBalanceGetRequest(SdkBaseModel):
    """Defines the request schema for ``/bank_transfer/balance/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    origination_account_id: OptionalNullable[str] = UNSET
    """If multiple origination accounts are available, ``origination_account_id`` must be used to specify the account
    for which balance will be returned."""


class BankTransferBalanceGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    origination_account_id: NotRequired[str | None]
