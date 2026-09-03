from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class RoleDetail(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    party_role_type: Literal["Borrower"] = Field(default="Borrower", alias="PartyRoleType")
    """A value from a MISMO defined list that identifies the role that the party plays in the transaction. Parties may
    be either a person or legal entity. A party may play multiple roles in a transaction."""


class RoleDetailDict(TypedDict):
    party_role_type: NotRequired[Literal["Borrower"]]
