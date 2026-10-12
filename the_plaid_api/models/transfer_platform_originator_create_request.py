from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .tosacceptance_metadata import TosacceptanceMetadata, TosacceptanceMetadataDict


class TransferPlatformOriginatorCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/platform/originator/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """The client ID of the originator"""

    tos_acceptance_metadata: TosacceptanceMetadata
    """Metadata related to the acceptance of Terms of Service"""

    originator_reviewed_at: RFC3339DateTime
    """ISO8601 timestamp indicating the most recent time the platform collected onboarding data from the originator"""

    webhook: Optional[str] = UNSET
    """The webhook URL to which a ``PLATFORM_ONBOARDING_UPDATE`` webhook should be sent."""


class TransferPlatformOriginatorCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    tos_acceptance_metadata: TosacceptanceMetadataDict
    originator_reviewed_at: RFC3339DateTime
    webhook: NotRequired[str]
