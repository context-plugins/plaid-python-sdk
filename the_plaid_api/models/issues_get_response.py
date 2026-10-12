from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue import Issue, IssueDict


class IssuesGetResponse(SdkBaseModel):
    """IssuesGetResponse defines the response schema for ``/issues/get``."""

    issue: Optional[Issue] = UNSET
    """Information on an issue encountered with financial institution interactions during Linking."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IssuesGetResponseDict(TypedDict):
    issue: NotRequired[IssueDict]
    request_id: NotRequired[str]
