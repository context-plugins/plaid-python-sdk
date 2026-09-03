from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferIntentCreateNetwork(str, Enum):
    """The network or rails used for the transfer. Defaults to ``same-day-ach``.

    For transfers submitted using ``ach``, the Standard ACH cutoff is 8:30 PM Eastern Time.

    For transfers submitted using ``same-day-ach``, the Same Day ACH cutoff is 3:00 PM Eastern Time. It is recommended
    to send the request 15 minutes prior to the cutoff to ensure that it will be processed in time for submission before
    the cutoff. If the transfer is processed after this cutoff but before the Standard ACH cutoff, it will be sent over
    Standard ACH rails and will not incur same-day charges.

    For transfers submitted using ``rtp``, in the case that the account being credited does not support RTP, the
    transfer will be sent over ACH as long as an ``ach_class`` is provided in the request. If RTP isn't supported by the
    account and no ``ach_class`` is provided, the transfer will fail to be submitted."""

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"
    RTP = "rtp"

    __str__ = str.__str__


TransferIntentCreateNetworkOrStr: TypeAlias = Annotated[
    TransferIntentCreateNetwork | str, open_enum_validator(TransferIntentCreateNetwork)
]
