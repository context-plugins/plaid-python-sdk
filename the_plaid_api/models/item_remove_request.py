from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.item_remove_reason_code import ItemRemoveReasonCodeOrStr


class ItemRemoveRequest(SdkBaseModel):
    """ItemRemoveRequest defines the request schema for ``/item/remove``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    reason_code: OptionalNullable[ItemRemoveReasonCodeOrStr] = UNSET
    """The reason for removing the Item

    ``FRAUD_FIRST_PARTY``: The end user who owns the connected bank account committed fraud ``FRAUD_FALSE_IDENTITY``:
    The end user created the connection using false identity information or stolen credentials ``FRAUD_ABUSE``: The end
    user is abusing the client's service or platform through their connected account ``FRAUD_OTHER``: Other
    fraud-related reasons involving the end user not covered by the specific fraud categories
    ``CONNECTION_IS_NON_FUNCTIONAL``: The connection to the end user's financial institution is broken and cannot be
    restored ``OTHER``: Any other reason for removing the connection not covered by the above categories"""

    reason_note: OptionalNullable[str] = UNSET
    """Additional context or details about the reason for removing the Item. Personally identifiable information, such
    as an email address or phone number, should not be included in the ``reason_note``."""


class ItemRemoveRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    reason_code: NotRequired[ItemRemoveReasonCodeOrStr | None]
    reason_note: NotRequired[str | None]
