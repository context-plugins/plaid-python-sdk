from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SessionTokenCreateRequestUser(SdkBaseModel):
    """Details about the end user. Required if a root-level ``user_id`` is not provided."""

    client_user_id: str
    """A unique ID representing the end user. Typically this will be a user ID number from your application. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``. It
    is currently used as a means of searching logs for the given user in the Plaid Dashboard."""

    user_id: Optional[str] = UNSET


class SessionTokenCreateRequestUserDict(TypedDict):
    client_user_id: str
    user_id: NotRequired[str]
