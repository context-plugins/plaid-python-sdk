from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditAuditCopyTokenCreateRequest(SdkBaseModel):
    """CreditAuditCopyTokenCreateRequest defines the request schema for ``/credit/audit_copy_token/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    report_tokens: list[str]
    """List of report tokens; can include at most one VOA/standard Asset Report tokens and one VOE Asset Report
    Token."""


class CreditAuditCopyTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    report_tokens: list[str]
