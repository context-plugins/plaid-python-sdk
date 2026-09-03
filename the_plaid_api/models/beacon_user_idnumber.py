from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.idnumber_type import IdnumberTypeOrStr


class BeaconUserIdnumber(SdkBaseModel):
    """The ID number associated with a Beacon User."""

    value: str
    """Value of the identity document typed in by the user. Alpha-numeric, with all formatting characters stripped. For
    specific format requirements by ID type, see `Input Validation Rules
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#id-numbers>`__."""

    type_: IdnumberTypeOrStr = Field(alias="type")
    """A globally unique and human readable ID type, specific to the country and document category. For more context on
    this field, see `Input Validation Rules
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#id-numbers>`__."""


class BeaconUserIdnumberDict(TypedDict):
    value: str
    type_: IdnumberTypeOrStr
