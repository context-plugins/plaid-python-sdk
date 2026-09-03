from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkSessionSuccessMetadataTransferStatus(str, Enum):
    """The status of a transfer. Returned only when `Transfer UI <https://plaid.com/docs/transfer/using-transfer-ui>`__
    is implemented.

    - ``COMPLETE`` - The transfer was completed.
    - ``INCOMPLETE`` - The transfer could not be completed. For help, see `Troubleshooting transfers
        <https://plaid.com/docs/transfer/using-transfer-ui/#troubleshooting-transfer-ui>`__."""

    COMPLETE = "COMPLETE"
    INCOMPLETE = "INCOMPLETE"

    __str__ = str.__str__


LinkSessionSuccessMetadataTransferStatusOrStr: TypeAlias = Annotated[
    LinkSessionSuccessMetadataTransferStatus | str, open_enum_validator(LinkSessionSuccessMetadataTransferStatus)
]
