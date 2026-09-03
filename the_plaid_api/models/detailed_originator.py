from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.transfer_diligence_status import TransferDiligenceStatusOrStr
from .transfer_platform_requirement import TransferPlatformRequirement, TransferPlatformRequirementDict


class DetailedOriginator(SdkBaseModel):
    """Originator and their status."""

    client_id: str
    """Originator's client ID."""

    transfer_diligence_status: TransferDiligenceStatusOrStr
    """Originator's diligence status."""

    company_name: str
    """The company name of the end customer."""

    outstanding_requirements: Optional[list[TransferPlatformRequirement]] = UNSET
    """List of outstanding requirements that must be submitted before Plaid can approve the originator. Only populated
    when ``transfer_diligence_status`` is ``more_information_required``."""


class DetailedOriginatorDict(TypedDict):
    client_id: str
    transfer_diligence_status: TransferDiligenceStatusOrStr
    company_name: str
    outstanding_requirements: NotRequired[list[TransferPlatformRequirement | TransferPlatformRequirementDict]]
