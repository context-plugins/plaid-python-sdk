from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.issues_status import IssuesStatusOrStr


class Issue(SdkBaseModel):
    """Information on an issue encountered with financial institution interactions during Linking."""

    issue_id: Optional[str] = UNSET
    """The unique identifier of the issue."""

    institution_names: Optional[list[str]] = UNSET
    """A list of names of the financial institutions affected."""

    institution_ids: Optional[list[str]] = UNSET
    """A list of ids of the financial institutions affected."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """The creation time of the record tracking this issue."""

    summary: Optional[str] = UNSET
    """A simple summary of the error for the end user."""

    detailed_description: Optional[str] = UNSET
    """A more detailed description for the customer."""

    status: Optional[IssuesStatusOrStr] = UNSET
    """The current status of the issue."""


class IssueDict(TypedDict):
    issue_id: NotRequired[str]
    institution_names: NotRequired[list[str]]
    institution_ids: NotRequired[list[str]]
    created_at: NotRequired[RFC3339DateTime]
    summary: NotRequired[str]
    detailed_description: NotRequired[str]
    status: NotRequired[IssuesStatusOrStr]
