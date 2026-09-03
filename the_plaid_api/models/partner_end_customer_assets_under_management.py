from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PartnerEndCustomerAssetsUnderManagement(SdkBaseModel):
    """Assets under management for the given end customer. Required for end customers with monthly service
    commitments."""

    amount: float
    iso_currency_code: str


class PartnerEndCustomerAssetsUnderManagementDict(TypedDict):
    amount: float
    iso_currency_code: str
