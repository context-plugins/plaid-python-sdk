from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .numbers_ach import NumbersAch, NumbersAchDict
from .numbers_bacs import NumbersBacs, NumbersBacsDict
from .numbers_eft import NumbersEft, NumbersEftDict
from .numbers_international import NumbersInternational, NumbersInternationalDict


class AuthGetNumbers(SdkBaseModel):
    """An object containing identifying numbers used for making electronic transfers to and from the ``accounts``. The
    identifying number type (ACH, EFT, IBAN, or Bacs) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by any ``accounts`` for which
    data has been requested, the array for that type will be empty."""

    ach: list[NumbersAch]
    """An array of ACH numbers identifying accounts."""

    eft: list[NumbersEft]
    """An array of EFT numbers identifying accounts."""

    international: list[NumbersInternational]
    """An array of IBAN numbers identifying accounts."""

    bacs: list[NumbersBacs]
    """An array of Bacs numbers identifying accounts."""


class AuthGetNumbersDict(TypedDict):
    ach: list[NumbersAchDict]
    eft: list[NumbersEftDict]
    international: list[NumbersInternationalDict]
    bacs: list[NumbersBacsDict]
