from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.plaid_error_type import PlaidErrorTypeOrStr


class CheckReportRepairableItem(SdkBaseModel):
    """An error object plus the ``item_id`` of an Item that the end user can repair via Link `update mode
    <https://plaid.com/docs/link/update-mode>`__. The ``error_code`` will be in the ``ITEM_LOGIN_REQUIRED`` family."""

    error_type: PlaidErrorTypeOrStr
    """A broad categorization of the error. Safe for programmatic use."""

    error_code: str
    """The particular error code. Safe for programmatic use."""

    error_message: str
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic
    use."""

    display_message: str | None
    """A user-friendly representation of the error code. ``null`` if the error is not related to user action."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class CheckReportRepairableItemDict(TypedDict):
    error_type: PlaidErrorTypeOrStr
    error_code: str
    error_message: str
    display_message: str | None
    item_id: str
