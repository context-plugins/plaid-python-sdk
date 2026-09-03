from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditAuditCopyTokenUpdateResponse(SdkBaseModel):
    """Defines the response schema for ``/credit/audit_copy_token/update``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    updated: bool
    """``true`` if the Audit Copy Token was successfully updated."""


class CreditAuditCopyTokenUpdateResponseDict(TypedDict):
    request_id: str
    updated: bool
