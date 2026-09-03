from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferIntentStatus(str, Enum):
    """The status of the transfer intent.

    ``PENDING``: The transfer intent is pending. ``SUCCEEDED``: The transfer intent was successfully created.
    ``FAILED``: The transfer intent was unable to be created."""

    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

    __str__ = str.__str__


TransferIntentStatusOrStr: TypeAlias = Annotated[TransferIntentStatus | str, open_enum_validator(TransferIntentStatus)]
