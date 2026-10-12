from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_funding_account_with_display_name import (
    TransferFundingAccountWithDisplayName,
    TransferFundingAccountWithDisplayNameDict,
)


class TransferOriginatorFundingAccountCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/originator/funding_account/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """The Plaid client ID of the transfer originator."""

    funding_account: TransferFundingAccountWithDisplayName
    """The originator's funding account, linked with Plaid Link or ``/transfer/migrate_account``."""


class TransferOriginatorFundingAccountCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    funding_account: TransferFundingAccountWithDisplayNameDict
