from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateInstitutionData(SdkBaseModel):
    """A map containing data used to highlight institutions in Link."""

    routing_number: Optional[str] = UNSET
    """The routing number of the bank to highlight in Link. Note: in rare cases, a single routing number can be
    associated with multiple institutions, e.g. due to a brokerage using another institution to manage ACH on its sweep
    accounts. If this happens, the bank will not be highlighted in Link even if the routing number is provided."""


class LinkTokenCreateInstitutionDataDict(TypedDict):
    routing_number: NotRequired[str]
