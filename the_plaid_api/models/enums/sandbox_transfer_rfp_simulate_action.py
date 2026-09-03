from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxTransferRfpSimulateAction(str, Enum):
    """The action to simulate. Must be either ``approve`` or ``reject``.

    - ``approve``: Simulates bank approval, transitioning the transfer to ``settled`` status
    - ``reject``: Simulates bank rejection, transitioning the transfer to ``failed`` status"""

    APPROVE = "approve"
    REJECT = "reject"

    __str__ = str.__str__


SandboxTransferRfpSimulateActionOrStr: TypeAlias = Annotated[
    SandboxTransferRfpSimulateAction | str, open_enum_validator(SandboxTransferRfpSimulateAction)
]
