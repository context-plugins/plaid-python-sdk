from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ItemApplicationListUserAuth(SdkBaseModel):
    """User authentication parameters, for clients making a request without an ``access_token``. This is only allowed
    for select clients and will not be supported in the future. Most clients should call ``/item/import`` to obtain an
    access token before making a request."""

    user_id: OptionalNullable[str] = UNSET
    """Account username."""

    fi_username_hash: OptionalNullable[str] = UNSET
    """Account username hashed by FI."""


class ItemApplicationListUserAuthDict(TypedDict):
    user_id: NotRequired[str | None]
    fi_username_hash: NotRequired[str | None]
