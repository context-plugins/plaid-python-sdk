from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClientCustomization(SdkBaseModel):
    """Custom client fields"""

    custom_entity_id: Optional[str] = UNSET
    """Custom entity ID that maps to a merchant or counterparty. This is different from the ``merchant_entity_id`` as
    well as the ``entity_id`` on the counterparties object to meet client specific needs."""


class ClientCustomizationDict(TypedDict):
    custom_entity_id: NotRequired[str]
