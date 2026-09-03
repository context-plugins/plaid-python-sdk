from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PendingDisconnectWebhookReason(str, Enum):
    """Reason why the Item is about to be disconnected. ``INSTITUTION_MIGRATION``: The institution is moving to API or
    to a different integration. For example, this can occur when an institution moves from a non-OAuth integration to an
    OAuth integration. ``INSTITUTION_TOKEN_EXPIRATION``: The consent on an Item associated with a US or CA institution
    is about to expire."""

    INSTITUTION_MIGRATION = "INSTITUTION_MIGRATION"
    INSTITUTION_TOKEN_EXPIRATION = "INSTITUTION_TOKEN_EXPIRATION"

    __str__ = str.__str__


PendingDisconnectWebhookReasonOrStr: TypeAlias = Annotated[
    PendingDisconnectWebhookReason | str, open_enum_validator(PendingDisconnectWebhookReason)
]
