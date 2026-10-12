from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_verification_of_asset import (
    CreditFreddieMacVerificationOfAsset,
    CreditFreddieMacVerificationOfAssetDict,
)
from .statuses import Statuses, StatusesDict


class CreditFreddieMacService(SdkBaseModel):
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""

    verification_of_asset: list[CreditFreddieMacVerificationOfAsset] = Field(alias="VERIFICATION_OF_ASSET")
    statuses: Statuses = Field(alias="STATUSES")
    """A collection of STATUS containers."""


class CreditFreddieMacServiceDict(TypedDict):
    verification_of_asset: list[CreditFreddieMacVerificationOfAssetDict]
    statuses: StatusesDict
