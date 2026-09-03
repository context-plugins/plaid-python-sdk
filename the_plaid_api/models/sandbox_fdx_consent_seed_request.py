from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxFdxConsentSeedRequest(SdkBaseModel):
    """Request to seed an FDX consent grant, and its backing item, for the given end user and recipient application so
    the FDX Consent API can be exercised in Sandbox."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    customer_id: str
    """The data provider's identifier for the end user to associate the seeded consent grant with."""

    application_id: str
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""

    consent_id: Optional[str] = UNSET
    """Optional UUIDv4 identifier for the seeded consent grant. If omitted, one is generated. Seeding fails if a grant
    with this identifier already exists."""


class SandboxFdxConsentSeedRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    customer_id: str
    application_id: str
    consent_id: NotRequired[str]
