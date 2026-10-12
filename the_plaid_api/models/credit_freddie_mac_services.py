from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_service import CreditFreddieMacService, CreditFreddieMacServiceDict


class CreditFreddieMacServices(SdkBaseModel):
    """A collection of objects that describe requests and responses for services."""

    service: CreditFreddieMacService = Field(alias="SERVICE")
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""


class CreditFreddieMacServicesDict(TypedDict):
    service: CreditFreddieMacServiceDict
