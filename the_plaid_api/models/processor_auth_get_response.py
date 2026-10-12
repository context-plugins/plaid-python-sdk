from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .processor_number import ProcessorNumber, ProcessorNumberDict


class ProcessorAuthGetResponse(SdkBaseModel):
    """ProcessorAuthGetResponse defines the response schema for ``/processor/auth/get``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    numbers: ProcessorNumber
    """An object containing identifying numbers used for making electronic transfers to and from the ``account``. The
    identifying number type (ACH, EFT, IBAN, or Bacs) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by the ``account`` for which
    auth data has been requested, a null value will be returned."""

    account: Account
    """A single account at a financial institution."""


class ProcessorAuthGetResponseDict(TypedDict):
    request_id: str
    numbers: ProcessorNumberDict
    account: AccountDict
