from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.fdx_consent_resource_type import FdxConsentResourceTypeOrStr
from .enums.fdx_data_cluster import FdxDataClusterOrStr


class FdxconsentGrantResource(SdkBaseModel):
    """One permissioned resource on a consent grant."""

    resource_type: FdxConsentResourceTypeOrStr = Field(alias="resourceType")
    """Type of resource permissioned on a consent grant."""

    resource_id: str = Field(alias="resourceId")
    """Identifier of the resource permissioned."""

    data_clusters: list[FdxDataClusterOrStr] = Field(alias="dataClusters")
    """Names of clusters of data elements permissioned."""


class FdxconsentGrantResourceDict(TypedDict):
    resource_type: FdxConsentResourceTypeOrStr
    resource_id: str
    data_clusters: list[FdxDataClusterOrStr]
