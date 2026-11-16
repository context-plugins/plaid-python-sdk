from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fdx_consent_grant import FdxConsentGrant, FdxConsentGrantDict


class GetConsentsResponse(SdkBaseModel):
    """GetConsentsResponse defines the response schema for ``/fdx/consents``"""

    consent_grants: list[FdxConsentGrant]
    """Consent grants matching the customerId (and optional status) filter."""


class GetConsentsResponseDict(TypedDict):
    consent_grants: list[FdxConsentGrantDict]
