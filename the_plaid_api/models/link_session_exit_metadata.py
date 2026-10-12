from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .link_session_exit_metadata_institution import (
    LinkSessionExitMetadataInstitution,
    LinkSessionExitMetadataInstitutionDict,
)
from .status2 import Status2, Status2Dict


class LinkSessionExitMetadata(SdkBaseModel):
    """Displayed if a user exits Link without successfully linking an Item."""

    institution: OptionalNullable[LinkSessionExitMetadataInstitution] = UNSET
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""

    status: Optional[Status2] = UNSET
    """The point at which the user exited the Link flow. One of the following values."""

    link_session_id: Optional[str] = UNSET
    """A unique identifier associated with a user's actions and events through the Link flow. Include this identifier
    when opening a support ticket for faster turnaround."""

    request_id: Optional[str] = UNSET
    """The request ID for the last request made by Link. This can be shared with Plaid support to expedite
    investigation."""


class LinkSessionExitMetadataDict(TypedDict):
    institution: NotRequired[LinkSessionExitMetadataInstitutionDict | None]
    status: NotRequired[Status2Dict]
    link_session_id: NotRequired[str]
    request_id: NotRequired[str]
