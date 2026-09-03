from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class IssueResolvedWebhook(SdkBaseModel):
    """Webhook notifications are sent only when a subscribed issue is marked as resolved. The payload contains details
    about the issue at the time of its resolution, focusing on the most essential information."""

    webhook_type: str
    """``ISSUES``"""

    webhook_code: str
    """``ISSUE_RESOLVED``"""

    issue_id: str
    """The unique identifier of the connectivity issue."""

    issue_description: str
    """A simple description of the error for the end user."""

    issue_resolved_at: RFC3339DateTime
    """The time when the issue was marked as resolved."""

    institution_id: str
    """The unique identifier of the financial institution involved."""

    institution_name: str
    """The name of the financial institution involved."""


class IssueResolvedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    issue_id: str
    issue_description: str
    issue_resolved_at: RFC3339DateTime
    institution_id: str
    institution_name: str
