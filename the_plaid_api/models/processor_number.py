from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .numbers_ach_nullable import NumbersAchNullable, NumbersAchNullableDict
from .numbers_bacs_nullable import NumbersBacsNullable, NumbersBacsNullableDict
from .numbers_eft_nullable import NumbersEftNullable, NumbersEftNullableDict
from .numbers_international_nullable import NumbersInternationalNullable, NumbersInternationalNullableDict


class ProcessorNumber(SdkBaseModel):
    """An object containing identifying numbers used for making electronic transfers to and from the ``account``. The
    identifying number type (ACH, EFT, IBAN, or Bacs) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by the ``account`` for which
    auth data has been requested, a null value will be returned."""

    ach: OptionalNullable[NumbersAchNullable] = UNSET
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""

    eft: OptionalNullable[NumbersEftNullable] = UNSET
    """Identifying information for transferring money to or from a Canadian bank account via EFT."""

    international: OptionalNullable[NumbersInternationalNullable] = UNSET
    """Identifying information for transferring money to or from an international bank account via wire transfer."""

    bacs: OptionalNullable[NumbersBacsNullable] = UNSET
    """Identifying information for transferring money to or from a UK bank account via Bacs."""


class ProcessorNumberDict(TypedDict):
    ach: NotRequired[NumbersAchNullableDict | None]
    eft: NotRequired[NumbersEftNullableDict | None]
    international: NotRequired[NumbersInternationalNullableDict | None]
    bacs: NotRequired[NumbersBacsNullableDict | None]
