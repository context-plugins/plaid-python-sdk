from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link_session_success_metadata_account import (
    LinkSessionSuccessMetadataAccount,
    LinkSessionSuccessMetadataAccountDict,
)
from .link_session_success_metadata_institution import (
    LinkSessionSuccessMetadataInstitution,
    LinkSessionSuccessMetadataInstitutionDict,
)


class LinkSessionItemAddResult(SdkBaseModel):
    """The details of an Item add in Link."""

    public_token: str
    """Returned once a user has successfully linked their Item."""

    accounts: list[LinkSessionSuccessMetadataAccount]
    """A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard,
    ``accounts`` will only include selected accounts."""

    institution: LinkSessionSuccessMetadataInstitution | None
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""


class LinkSessionItemAddResultDict(TypedDict):
    public_token: str
    accounts: list[LinkSessionSuccessMetadataAccountDict]
    institution: LinkSessionSuccessMetadataInstitutionDict | None
