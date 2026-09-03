from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestPaymentInitiation(SdkBaseModel):
    """Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is
    required if ``payment_initiation`` is included in the ``products`` array. Either ``payment_id`` or ``consent_id``
    must be provided."""

    payment_id: Optional[str] = UNSET
    """The ``payment_id`` provided by the ``/payment_initiation/payment/create`` endpoint."""

    consent_id: Optional[str] = UNSET
    """The ``consent_id`` provided by the ``/payment_initiation/consent/create`` endpoint."""


class LinkTokenCreateRequestPaymentInitiationDict(TypedDict):
    payment_id: NotRequired[str]
    consent_id: NotRequired[str]
