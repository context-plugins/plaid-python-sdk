from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fdxconsent_revocation_record import FdxconsentRevocationRecord, FdxconsentRevocationRecordDict


class FdxconsentRevocations(SdkBaseModel):
    """The revocation history of a consent grant. Response body for GET /fdx/consents/{consentId}/revocation."""

    revocations: list[FdxconsentRevocationRecord]
    """Revocation records for the consent grant, most recent first. Empty when the grant has never been revoked."""


class FdxconsentRevocationsDict(TypedDict):
    revocations: list[FdxconsentRevocationRecordDict]
