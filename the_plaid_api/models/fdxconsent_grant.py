from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.fdx_consent_grant_status import FdxConsentGrantStatusOrStr
from .fdxconsent_grant_resource import FdxconsentGrantResource, FdxconsentGrantResourceDict
from .party_entity import PartyEntity, PartyEntityDict


class FdxconsentGrant(SdkBaseModel):
    """An FDX consent grant."""

    id: str
    """The persistent identifier of the consent grant"""

    status: FdxConsentGrantStatusOrStr
    """Current status of a consent grant. One of ``ACTIVE``, ``REVOKED``, ``EXPIRED``."""

    created_time: RFC3339DateTime = Field(alias="createdTime")
    """When the consent was initially granted"""

    updated_time: RFC3339DateTime = Field(alias="updatedTime")
    """When the consent grant was last updated"""

    expiration_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expirationTime")
    """When the consent grant will expire. Omitted when the grant has no expiration."""

    parties: list[PartyEntity]
    """Non-end-user parties participating in the consent grant (Data Recipient, Data Provider, Data Access Platform)."""

    resources: Optional[list[FdxconsentGrantResource]] = UNSET
    """Permissioned resource entries. Omitted when there are no resources."""


class FdxconsentGrantDict(TypedDict):
    id: str
    status: FdxConsentGrantStatusOrStr
    created_time: RFC3339DateTime
    updated_time: RFC3339DateTime
    expiration_time: NotRequired[RFC3339DateTime]
    parties: list[PartyEntityDict]
    resources: NotRequired[list[FdxconsentGrantResourceDict]]
