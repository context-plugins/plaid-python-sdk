from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.content_types import ContentTypesOrStr
from .enums.fdxhateoas_link_action import FdxhateoasLinkActionOrStr


class HateoasLink(SdkBaseModel):
    """REST application constraint (Hypermedia As The Engine Of Application State)"""

    href: str
    """URL to invoke the action on the resource"""

    action: Optional[FdxhateoasLinkActionOrStr] = UNSET
    """HTTP Method to use for the request"""

    rel: Optional[str] = UNSET
    """Relation of this link to its containing entity, as defined by and with many example relation values at `IETF
    RFC5988 <https://datatracker.ietf.org/doc/html/rfc5988>`__"""

    types: Optional[list[ContentTypesOrStr]] = UNSET
    """Content-types that can be used in the Accept header"""


class HateoasLinkDict(TypedDict):
    href: str
    action: NotRequired[FdxhateoasLinkActionOrStr]
    rel: NotRequired[str]
    types: NotRequired[list[ContentTypesOrStr]]
