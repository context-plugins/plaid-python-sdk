from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue import Issue, IssueDict


class IssuesSearchResponse(SdkBaseModel):
    """IssuesSearchResponse defines the response schema for ``/issues/search``."""

    issues: Optional[list[Issue]] = UNSET
    """A list of issues affecting the Item, session, or request passed in, conforming to the Issues data model. An empty
    list indicates that no matching issues were found."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IssuesSearchResponseDict(TypedDict):
    issues: NotRequired[list[Issue | IssueDict]]
    request_id: NotRequired[str]
