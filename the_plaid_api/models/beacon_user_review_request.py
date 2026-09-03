from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.beacon_user_status import BeaconUserStatusOrStr


class BeaconUserReviewRequest(SdkBaseModel):
    """Request input for updating the status of a Beacon User"""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    status: BeaconUserStatusOrStr
    """A status of a Beacon User.

    ``rejected``: The Beacon User has been rejected for fraud. Users can be automatically or manually rejected.

    ``pending_review``: The Beacon User has been marked for review.

    ``cleared``: The Beacon User has been cleared of fraud."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BeaconUserReviewRequestDict(TypedDict):
    beacon_user_id: str
    status: BeaconUserStatusOrStr
    client_id: NotRequired[str]
    secret: NotRequired[str]
