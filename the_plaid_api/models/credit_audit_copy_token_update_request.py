from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditAuditCopyTokenUpdateRequest(SdkBaseModel):
    """CreditAuditCopyTokenUpdateRequest defines the request schema for ``/credit/audit_copy_token/update``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    audit_copy_token: str
    """The ``audit_copy_token`` you would like to update."""

    report_tokens: list[str]
    """Array of tokens which the specified Audit Copy Token will be updated with. The types of token supported are asset
    report token and employment report token. There can be at most 1 of each token type in the array."""


class CreditAuditCopyTokenUpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    audit_copy_token: str
    report_tokens: list[str]
