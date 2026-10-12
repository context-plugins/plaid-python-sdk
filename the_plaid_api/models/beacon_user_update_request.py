from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .beacon_user_update_request_data import BeaconUserUpdateRequestData, BeaconUserUpdateRequestDataDict


class BeaconUserUpdateRequest(SdkBaseModel):
    """Request input for updating the identity data of a Beacon User."""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    user: OptionalNullable[BeaconUserUpdateRequestData] = UNSET
    """A subset of a Beacon User's data which is used to patch the existing identity data associated with a Beacon User.
    At least one field must be provided. If left unset or null, user data will not be patched."""

    access_tokens: OptionalNullable[list[str]] = UNSET
    """Send this array of access tokens to add accounts to this user for evaluation. This will add accounts to this
    Beacon User. If left null only existing accounts will be returned in response. A maximum of 50 accounts total can be
    added to a Beacon User."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BeaconUserUpdateRequestDict(TypedDict):
    beacon_user_id: str
    user: NotRequired[BeaconUserUpdateRequestDataDict | None]
    access_tokens: NotRequired[list[str] | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
