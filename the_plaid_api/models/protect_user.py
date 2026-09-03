from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProtectUser(SdkBaseModel):
    """Represents an end user for ``/protect/compute`` requests."""

    user_id: Optional[str] = UNSET
    """The Plaid User ID returned from a previous call to ``/user/create``. This or ``client_user_id`` can be provided,
    not both."""

    client_user_id: Optional[str] = UNSET
    """A unique ID representing the end user, previously passed to ``/user/create``. Maximum of 128 characters.
    Typically this will be a user ID number from your application. Personally identifiable information, such as an email
    address or phone number, should not be used in the ``client_user_id``."""


class ProtectUserDict(TypedDict):
    user_id: NotRequired[str]
    client_user_id: NotRequired[str]
