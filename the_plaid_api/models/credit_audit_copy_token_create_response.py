from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditAuditCopyTokenCreateResponse(SdkBaseModel):
    """CreditAuditCopyTokenCreateResponse defines the response schema for ``/credit/audit_copy_token/create``"""

    audit_copy_token: str
    """A token that can be shared with a third party auditor, which allows them to fetch the Asset Reports attached to
    the token. This token should be stored securely."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditAuditCopyTokenCreateResponseDict(TypedDict):
    audit_copy_token: str
    request_id: str
