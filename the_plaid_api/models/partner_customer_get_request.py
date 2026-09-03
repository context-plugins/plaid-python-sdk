from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerCustomerGetRequest(SdkBaseModel):
    """Request schema for ``/partner/customer/get``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    end_customer_client_id: str


class PartnerCustomerGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    end_customer_client_id: str
