from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class PaymentConsentValidDateTime(SdkBaseModel):
    """Life span for the payment consent. After the ``to`` date the payment consent expires and can no longer be used
    for payment initiation."""

    from_: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="from")
    """The date and time from which the consent should be active, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format."""

    to: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time at which the consent expires, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""


class PaymentConsentValidDateTimeDict(TypedDict):
    from_: NotRequired[RFC3339DateTime | None]
    to: NotRequired[RFC3339DateTime | None]
