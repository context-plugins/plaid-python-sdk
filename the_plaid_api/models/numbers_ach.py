from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class NumbersAch(SdkBaseModel):
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The ACH account number for the account.

    At certain institutions, including Chase, PNC, and US Bank, you will receive a "tokenized" account number, which is
    not the user's actual account number. For important details on how this may impact your integration and on how to
    avoid fraud, user confusion, and ACH returns, see `Tokenized account numbers
    <https://plaid.com/docs/auth/#tokenized-account-numbers>`__."""

    is_tokenized_account_number: Optional[bool] = UNSET
    """Indicates whether the account number is tokenized by the institution. For important details on how tokenized
    account numbers may impact your integration, see `Tokenized account numbers
    <https://plaid.com/docs/auth/#tokenized-account-numbers>`__."""

    routing: str
    """The ACH routing number for the account. For more information, see `Tokenized account numbers
    <https://plaid.com/docs/auth/#tokenized-account-numbers>`__."""

    wire_routing: str | None
    """The wire transfer routing number for the account. This field is only populated if the institution is known to use
    a separate wire transfer routing number. Many institutions do not have a separate wire routing number and use the
    ACH routing number for wires instead. It is recommended to have the end user manually confirm their wire routing
    number before sending any wires to their account, especially if this field is ``null``."""

    can_transfer_in: OptionalNullable[bool] = UNSET
    """Whether the account supports ACH transfers into the account"""

    can_transfer_out: OptionalNullable[bool] = UNSET
    """Whether the account supports ACH transfers out of the account"""


class NumbersAchDict(TypedDict):
    account_id: str
    account: str
    is_tokenized_account_number: NotRequired[bool]
    routing: str
    wire_routing: str | None
    can_transfer_in: NotRequired[bool | None]
    can_transfer_out: NotRequired[bool | None]
