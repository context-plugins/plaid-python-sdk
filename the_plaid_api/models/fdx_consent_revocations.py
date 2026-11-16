from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fdx_consent_revocation_record import FdxConsentRevocationRecord, FdxConsentRevocationRecordDict


class FdxConsentRevocations(SdkBaseModel):
    """The revocation history of a consent grant. Response body for GET /fdx/consents/{consentId}/revocation."""

    revocations: list[FdxConsentRevocationRecord]
    """Revocation records for the consent grant, most recent first. Empty when the grant has never been revoked."""


class FdxConsentRevocationsDict(TypedDict):
    revocations: list[FdxConsentRevocationRecordDict]
