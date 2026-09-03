from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.idnumber_type import IdnumberTypeOrStr


class TransferPlatformPersonIdnumber(SdkBaseModel):
    """ID number of the person"""

    value: str
    """Value of the person's ID Number. Alpha-numeric, with all formatting characters stripped."""

    type_: IdnumberTypeOrStr = Field(alias="type")
    """A globally unique and human readable ID type, specific to the country and document category. For more context on
    this field, see `Input Validation Rules
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#id-numbers>`__."""


class TransferPlatformPersonIdnumberDict(TypedDict):
    value: str
    type_: IdnumberTypeOrStr
