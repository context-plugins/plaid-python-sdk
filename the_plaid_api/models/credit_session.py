from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .credit_session_error import CreditSessionError, CreditSessionErrorDict
from .credit_session_results import CreditSessionResults, CreditSessionResultsDict


class CreditSession(SdkBaseModel):
    """Metadata and results for a Link session"""

    link_session_id: Optional[str] = UNSET
    """The unique identifier associated with the Link session. This identifier matches the ``link_session_id`` returned
    in the onSuccess/onExit callbacks."""

    session_start_time: Optional[RFC3339DateTime] = UNSET
    """The time when the Link session started"""

    results: Optional[CreditSessionResults] = UNSET
    """The set of results for a Link session."""

    errors: Optional[list[CreditSessionError]] = UNSET
    """The set of errors that occurred during the Link session."""


class CreditSessionDict(TypedDict):
    link_session_id: NotRequired[str]
    session_start_time: NotRequired[RFC3339DateTime]
    results: NotRequired[CreditSessionResultsDict]
    errors: NotRequired[list[CreditSessionErrorDict]]
