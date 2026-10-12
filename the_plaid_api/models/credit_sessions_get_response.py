from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_session import CreditSession, CreditSessionDict


class CreditSessionsGetResponse(SdkBaseModel):
    """CreditSessionsGetResponse defines the response schema for ``/credit/sessions/get``"""

    sessions: Optional[list[CreditSession]] = UNSET
    """A list of Link sessions for the user. Sessions will be sorted in reverse chronological order."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditSessionsGetResponseDict(TypedDict):
    sessions: NotRequired[list[CreditSessionDict]]
    request_id: str
