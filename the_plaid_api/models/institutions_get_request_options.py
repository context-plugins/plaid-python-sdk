from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.products import ProductsOrStr


class InstitutionsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/institutions/get`` results."""

    products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """Filter the Institutions based on which products they support. Will only return institutions that support all
    listed products. When filtering based on ``auth``, an institution must support Instant Auth to match the criterion.
    To filter for Signal Transaction Scores support, use ``balance``. To filter for Transfer support, use ``auth``."""

    routing_numbers: OptionalNullable[list[str]] = UNSET
    """Specify an array of routing numbers to filter institutions. The response will only return institutions that match
    all of the routing numbers in the array. Routing number records used for this matching are generally comprehensive;
    however, failure to match a given routing number to an institution does not necessarily mean that the institution is
    unsupported by Plaid. Invalid routing numbers (numbers that are not 9 digits in length or do not have a valid
    checksum) will be filtered from the array before the response is processed. If all provided routing numbers are
    invalid, an ``INVALID_REQUEST`` error with the code of ``INVALID_FIELD`` will be returned."""

    oauth: OptionalNullable[bool] = UNSET
    """Limit results to institutions with or without OAuth login flows. Note that institutions will have ``oauth`` set
    to ``true`` if some Items associated with that institution are required to use OAuth flows; institutions in a state
    of migration to OAuth will have the ``oauth`` attribute set to ``true``."""

    include_optional_metadata: Optional[bool] = UNSET
    """When ``true``, return the institution's homepage URL, logo and primary brand color. Not all institutions' logos
    are available.

    Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you
    agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the
    appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied
    warranties with respect to the logos."""

    include_auth_metadata: bool = False
    """When ``true``, returns metadata related to the Auth product indicating which auth methods are supported."""

    include_payment_initiation_metadata: bool = False
    """When ``true``, returns metadata related to the Payment Initiation product indicating which payment configurations
    are supported."""


class InstitutionsGetRequestOptionsDict(TypedDict):
    products: NotRequired[list[ProductsOrStr] | None]
    routing_numbers: NotRequired[list[str] | None]
    oauth: NotRequired[bool | None]
    include_optional_metadata: NotRequired[bool]
    include_auth_metadata: NotRequired[bool]
    include_payment_initiation_metadata: NotRequired[bool]
