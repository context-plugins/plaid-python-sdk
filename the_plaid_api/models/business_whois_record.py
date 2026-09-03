from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class BusinessWhoisRecord(SdkBaseModel):
    """WHOIS metadata for the business website domain."""

    domain_created_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    domain_updated_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    domain_expires_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    registrar: str | None
    """Domain registrar."""


class BusinessWhoisRecordDict(TypedDict):
    domain_created_at: RFC3339DateTime | None
    domain_updated_at: RFC3339DateTime | None
    domain_expires_at: RFC3339DateTime | None
    registrar: str | None
