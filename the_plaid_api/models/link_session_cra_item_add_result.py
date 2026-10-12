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


class LinkSessionCraItemAddResult(SdkBaseModel):
    """The details of a Plaid Check Item add in Link."""

    item_id: str
    """The Plaid Check Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice
    will result in two Items with different ``item_id`` values. The ``item_id`` is case-sensitive."""

    accounts: list[LinkSessionSuccessMetadataAccount]
    """A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard,
    ``accounts`` will only include selected accounts."""

    institution: LinkSessionSuccessMetadataInstitution | None
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""


class LinkSessionCraItemAddResultDict(TypedDict):
    item_id: str
    accounts: list[LinkSessionSuccessMetadataAccountDict]
    institution: LinkSessionSuccessMetadataInstitutionDict | None
