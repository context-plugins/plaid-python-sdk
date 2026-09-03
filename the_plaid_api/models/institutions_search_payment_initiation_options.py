from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InstitutionsSearchPaymentInitiationOptions(SdkBaseModel):
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""

    payment_id: OptionalNullable[str] = UNSET
    """A unique ID identifying the payment"""

    consent_id: OptionalNullable[str] = UNSET
    """A unique ID identifying the payment consent"""


class InstitutionsSearchPaymentInitiationOptionsDict(TypedDict):
    payment_id: NotRequired[str | None]
    consent_id: NotRequired[str | None]
