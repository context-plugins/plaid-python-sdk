from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentsAuthOwner(SdkBaseModel):
    """Information on the ownership of an investment account"""

    account_id: Optional[str] = UNSET
    """The ID of the account that this identity information pertains to"""

    names: Optional[list[str]] = UNSET
    """A list of names associated with the account by the financial institution. In the case of a joint account, Plaid
    will make a best effort to report the names of all account holders.

    If an Item contains multiple accounts with different owner names, some institutions will report all names associated
    with the Item in each account's ``names`` array."""


class InvestmentsAuthOwnerDict(TypedDict):
    account_id: NotRequired[str]
    names: NotRequired[list[str]]
