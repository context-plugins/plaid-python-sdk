from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkSessionExitMetadataInstitution(SdkBaseModel):
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""

    name: Optional[str] = UNSET
    """The full institution name, such as ``Wells Fargo``"""

    institution_id: Optional[str] = UNSET
    """The Plaid institution identifier"""


class LinkSessionExitMetadataInstitutionDict(TypedDict):
    name: NotRequired[str]
    institution_id: NotRequired[str]
