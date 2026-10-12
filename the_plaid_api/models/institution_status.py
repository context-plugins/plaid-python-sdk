from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .health_incident import HealthIncident, HealthIncidentDict
from .product_status import ProductStatus, ProductStatusDict


class InstitutionStatus(SdkBaseModel):
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments
    updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and
    Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough
    traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate
    data.

    Institution status is accessible in the Dashboard and via the API using the ``/institutions/get_by_id`` endpoint
    with the ``options.include_status`` option set to true. Note that institution status is not available in the Sandbox
    environment."""

    item_logins: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    transactions_updates: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    auth: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    identity: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    investments_updates: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    liabilities_updates: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    liabilities: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    investments: OptionalNullable[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    health_incidents: OptionalNullable[list[HealthIncident]] = UNSET
    """Details of recent health incidents associated with the institution."""


class InstitutionStatusDict(TypedDict):
    item_logins: NotRequired[ProductStatusDict | None]
    transactions_updates: NotRequired[ProductStatusDict | None]
    auth: NotRequired[ProductStatusDict | None]
    identity: NotRequired[ProductStatusDict | None]
    investments_updates: NotRequired[ProductStatusDict | None]
    liabilities_updates: NotRequired[ProductStatusDict | None]
    liabilities: NotRequired[ProductStatusDict | None]
    investments: NotRequired[ProductStatusDict | None]
    health_incidents: NotRequired[list[HealthIncidentDict] | None]
