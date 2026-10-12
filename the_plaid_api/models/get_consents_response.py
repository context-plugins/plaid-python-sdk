from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fdxconsent_grant import FdxconsentGrant, FdxconsentGrantDict


class GetConsentsResponse(SdkBaseModel):
    """GetConsentsResponse defines the response schema for ``/fdx/consents``"""

    consent_grants: list[FdxconsentGrant]
    """Consent grants matching the customerId (and optional status) filter."""


class GetConsentsResponseDict(TypedDict):
    consent_grants: list[FdxconsentGrantDict]
