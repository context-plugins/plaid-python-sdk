from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .statuses import Statuses, StatusesDict
from .verification_of_asset import VerificationOfAsset, VerificationOfAssetDict


class Service(SdkBaseModel):
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""

    verification_of_asset: VerificationOfAsset = Field(alias="VERIFICATION_OF_ASSET")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    statuses: Statuses = Field(alias="STATUSES")
    """A collection of STATUS containers."""


class ServiceDict(TypedDict):
    verification_of_asset: VerificationOfAsset | VerificationOfAssetDict
    statuses: Statuses | StatusesDict
