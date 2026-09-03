from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferCapabilitiesGetRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/capabilities/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    payment_profile_token: Optional[str] = UNSET
    """A payment profile token associated with the Payment Profile data that is being requested."""


class TransferCapabilitiesGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    payment_profile_token: NotRequired[str]
