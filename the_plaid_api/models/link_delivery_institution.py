from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkDeliveryInstitution(SdkBaseModel):
    """Information related to the financial institution."""

    name: Optional[str] = UNSET
    """The full institution name, such as 'Wells Fargo'"""

    institution_id: Optional[str] = UNSET
    """The Plaid institution identifier"""


class LinkDeliveryInstitutionDict(TypedDict):
    name: NotRequired[str]
    institution_id: NotRequired[str]
