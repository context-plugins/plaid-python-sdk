from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .institutions_search_payment_initiation_options import (
    InstitutionsSearchPaymentInitiationOptions,
    InstitutionsSearchPaymentInitiationOptionsDict,
)


class InstitutionsSearchRequestOptions(SdkBaseModel):
    """An optional object to filter ``/institutions/search`` results."""

    oauth: OptionalNullable[bool] = UNSET
    """Limit results to institutions with or without OAuth login flows. Note that institutions will have ``oauth`` set
    to ``true`` if some Items associated with that institution are required to use OAuth flows; institutions in a state
    of migration to OAuth will have the ``oauth`` attribute set to ``true``."""

    include_optional_metadata: Optional[bool] = UNSET
    """When true, return the institution's homepage URL, logo and primary brand color."""

    include_auth_metadata: OptionalNullable[bool] = UNSET
    """When ``true``, returns metadata related to the Auth product indicating which auth methods are supported."""

    include_payment_initiation_metadata: OptionalNullable[bool] = UNSET
    """When ``true``, returns metadata related to the Payment Initiation product indicating which payment configurations
    are supported."""

    payment_initiation: OptionalNullable[InstitutionsSearchPaymentInitiationOptions] = UNSET
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""


class InstitutionsSearchRequestOptionsDict(TypedDict):
    oauth: NotRequired[bool | None]
    include_optional_metadata: NotRequired[bool]
    include_auth_metadata: NotRequired[bool | None]
    include_payment_initiation_metadata: NotRequired[bool | None]
    payment_initiation: NotRequired[
        InstitutionsSearchPaymentInitiationOptions | InstitutionsSearchPaymentInitiationOptionsDict | None
    ]
