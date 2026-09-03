from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .numbers_achnullable import NumbersAchnullable, NumbersAchnullableDict
from .numbers_bacsnullable import NumbersBacsnullable, NumbersBacsnullableDict
from .numbers_eftnullable import NumbersEftnullable, NumbersEftnullableDict
from .numbers_international_nullable import NumbersInternationalNullable, NumbersInternationalNullableDict


class ProcessorNumber(SdkBaseModel):
    """An object containing identifying numbers used for making electronic transfers to and from the ``account``. The
    identifying number type (ACH, EFT, IBAN, or Bacs) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by the ``account`` for which
    auth data has been requested, a null value will be returned."""

    ach: OptionalNullable[NumbersAchnullable] = UNSET
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""

    eft: OptionalNullable[NumbersEftnullable] = UNSET
    """Identifying information for transferring money to or from a Canadian bank account via EFT."""

    international: OptionalNullable[NumbersInternationalNullable] = UNSET
    """Identifying information for transferring money to or from an international bank account via wire transfer."""

    bacs: OptionalNullable[NumbersBacsnullable] = UNSET
    """Identifying information for transferring money to or from a UK bank account via Bacs."""


class ProcessorNumberDict(TypedDict):
    ach: NotRequired[NumbersAchnullable | NumbersAchnullableDict | None]
    eft: NotRequired[NumbersEftnullable | NumbersEftnullableDict | None]
    international: NotRequired[NumbersInternationalNullable | NumbersInternationalNullableDict | None]
    bacs: NotRequired[NumbersBacsnullable | NumbersBacsnullableDict | None]
