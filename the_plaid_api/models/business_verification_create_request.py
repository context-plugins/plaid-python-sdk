from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .business_verification_create_request_business import (
    BusinessVerificationCreateRequestBusiness,
    BusinessVerificationCreateRequestBusinessDict,
)


class BusinessVerificationCreateRequest(SdkBaseModel):
    """Request input for creating a business verification"""

    client_user_id: str
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    business: OptionalNullable[BusinessVerificationCreateRequestBusiness] = UNSET
    """Business information provided in the verification request"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BusinessVerificationCreateRequestDict(TypedDict):
    client_user_id: str
    business: NotRequired[BusinessVerificationCreateRequestBusinessDict | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
