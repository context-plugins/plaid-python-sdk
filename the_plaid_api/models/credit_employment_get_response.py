from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_employment_item import CreditEmploymentItem, CreditEmploymentItemDict


class CreditEmploymentGetResponse(SdkBaseModel):
    """CreditEmploymentGetResponse defines the response schema for ``/credit/employment/get``."""

    items: list[CreditEmploymentItem]
    """Array of employment items."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditEmploymentGetResponseDict(TypedDict):
    items: list[CreditEmploymentItem | CreditEmploymentItemDict]
    request_id: str
