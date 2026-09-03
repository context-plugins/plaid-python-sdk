from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .service import Service, ServiceDict


class Services(SdkBaseModel):
    """A collection of objects that describe requests and responses for services."""

    service: Service = Field(alias="SERVICE")
    """A collection of details related to a fulfillment service or product in terms of request, process and result."""


class ServicesDict(TypedDict):
    service: Service | ServiceDict
