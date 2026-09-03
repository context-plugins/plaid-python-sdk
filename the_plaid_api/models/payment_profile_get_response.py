from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.payment_profile_status import PaymentProfileStatusOrStr


class PaymentProfileGetResponse(SdkBaseModel):
    """PaymentProfileGetResponse defines the response schema for ``/payment_profile/get``"""

    updated_at: RFC3339DateTime
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    last time the given Payment Profile was updated at"""

    created_at: RFC3339DateTime
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    time the given Payment Profile was created at"""

    deleted_at: RFC3339DateTime | None
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    time the given Payment Profile was deleted at. Always ``null`` if the Payment Profile has not been deleted"""

    status: PaymentProfileStatusOrStr
    """The status of the given Payment Profile.

    ``READY``: This Payment Profile is ready to be used to create transfers using ``/transfer/authorization/create`` and
    ``/transfer/create``.

    ``PENDING``: This Payment Profile is not ready to be used. You'll need to call ``/link/token/create`` and provide
    the ``payment_profile_token`` in the ``transfer.payment_profile_token`` field to initiate the account linking
    experience.

    ``REMOVED``: This Payment Profile has been removed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentProfileGetResponseDict(TypedDict):
    updated_at: RFC3339DateTime
    created_at: RFC3339DateTime
    deleted_at: RFC3339DateTime | None
    status: PaymentProfileStatusOrStr
    request_id: str
