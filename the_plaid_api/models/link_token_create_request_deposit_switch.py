from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestDepositSwitch(SdkBaseModel):
    """(Deprecated) Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field
    is required if ``deposit_switch`` is included in the ``products`` array."""

    deposit_switch_id: str
    """The ``deposit_switch_id`` provided by the ``/deposit_switch/create`` endpoint."""


class LinkTokenCreateRequestDepositSwitchDict(TypedDict):
    deposit_switch_id: str
