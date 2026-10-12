from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.beacon_report_create_type import BeaconReportCreateTypeOrStr
from .fraud_amount import FraudAmount, FraudAmountDict


class BeaconReportCreateRequest(SdkBaseModel):
    """Request input for creating a Beacon Report"""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    type_: BeaconReportCreateTypeOrStr = Field(alias="type")
    """The type of Beacon Report.

    ``first_party``: If this is the same individual as the one who submitted the KYC.

    ``stolen``: If this is a different individual from the one who submitted the KYC.

    ``synthetic``: If this is an individual using fabricated information.

    ``account_takeover``: If this individual's account was compromised.

    ``unknown``: If you aren't sure who committed the fraud."""

    fraud_date: Date
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    fraud_amount: OptionalNullable[FraudAmount] = UNSET
    """The amount and currency of the fraud or attempted fraud. ``fraud_amount`` should be omitted to indicate an
    unknown fraud amount."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BeaconReportCreateRequestDict(TypedDict):
    beacon_user_id: str
    type_: BeaconReportCreateTypeOrStr
    fraud_date: Date
    fraud_amount: NotRequired[FraudAmountDict | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
