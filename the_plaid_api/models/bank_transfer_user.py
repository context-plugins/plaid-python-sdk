from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BankTransferUser(SdkBaseModel):
    """The legal name and other information for the account holder."""

    legal_name: str
    """The account holder's full legal name. If the transfer ``ach_class`` is ``ccd``, this should be the business name
    of the account holder."""

    email_address: OptionalNullable[str] = UNSET
    """The account holder's email."""

    routing_number: Optional[str] = UNSET
    """The account holder's routing number. This field is only used in response data. Do not provide this field when
    making requests."""


class BankTransferUserDict(TypedDict):
    legal_name: str
    email_address: NotRequired[str | None]
    routing_number: NotRequired[str]
