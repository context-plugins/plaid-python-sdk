from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentProfileStatus(str, Enum):
    """The status of the given Payment Profile.

    ``READY``: This Payment Profile is ready to be used to create transfers using ``/transfer/authorization/create`` and
    ``/transfer/create``.

    ``PENDING``: This Payment Profile is not ready to be used. You'll need to call ``/link/token/create`` and provide
    the ``payment_profile_token`` in the ``transfer.payment_profile_token`` field to initiate the account linking
    experience.

    ``REMOVED``: This Payment Profile has been removed."""

    PENDING = "PENDING"
    READY = "READY"
    REMOVED = "REMOVED"

    __str__ = str.__str__


PaymentProfileStatusOrStr: TypeAlias = Annotated[PaymentProfileStatus | str, open_enum_validator(PaymentProfileStatus)]
