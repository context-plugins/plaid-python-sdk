from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.link_session_success_metadata_transfer_status import LinkSessionSuccessMetadataTransferStatusOrStr
from .link_session_success_metadata_account import (
    LinkSessionSuccessMetadataAccount,
    LinkSessionSuccessMetadataAccountDict,
)
from .link_session_success_metadata_institution import (
    LinkSessionSuccessMetadataInstitution,
    LinkSessionSuccessMetadataInstitutionDict,
)


class LinkSessionSuccessMetadata(SdkBaseModel):
    """Displayed once a user has successfully linked their Item."""

    institution: OptionalNullable[LinkSessionSuccessMetadataInstitution] = UNSET
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""

    accounts: Optional[list[LinkSessionSuccessMetadataAccount]] = UNSET
    """A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard,
    ``accounts`` will only include selected accounts."""

    link_session_id: Optional[str] = UNSET
    """A unique identifier associated with a user's actions and events through the Link flow. Include this identifier
    when opening a support ticket for faster turnaround."""

    transfer_status: OptionalNullable[LinkSessionSuccessMetadataTransferStatusOrStr] = UNSET
    """The status of a transfer. Returned only when `Transfer UI <https://plaid.com/docs/transfer/using-transfer-ui>`__
    is implemented.

    - ``COMPLETE`` - The transfer was completed.
    - ``INCOMPLETE`` - The transfer could not be completed. For help, see `Troubleshooting transfers
        <https://plaid.com/docs/transfer/using-transfer-ui/#troubleshooting-transfer-ui>`__."""


class LinkSessionSuccessMetadataDict(TypedDict):
    institution: NotRequired[LinkSessionSuccessMetadataInstitutionDict | None]
    accounts: NotRequired[list[LinkSessionSuccessMetadataAccountDict]]
    link_session_id: NotRequired[str]
    transfer_status: NotRequired[LinkSessionSuccessMetadataTransferStatusOrStr | None]
