from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DocumentRiskSignalInstitutionMetadata(SdkBaseModel):
    """An object which contains additional metadata about the institution used to compute the verification attribute"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class DocumentRiskSignalInstitutionMetadataDict(TypedDict):
    item_id: str
