from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, RFC3339DateTime, SdkBaseModel
from .beacon_audit_trail import BeaconAuditTrail, BeaconAuditTrailDict
from .enums.beacon_report_type import BeaconReportTypeOrStr
from .fraud_amount import FraudAmount, FraudAmountDict


class BeaconReportCreateResponse(SdkBaseModel):
    """A Beacon Report describes the type of fraud committed by a user as well as the date the fraud was committed and
    the total amount of money lost due to the fraud incident.

    This information is used to block similar fraud attempts on your platform as well as alert other companies who
    screen a user with matching identity information. Other companies will not receive any new identity information,
    just what matched, plus information such as industry, type of fraud, and date of fraud.

    You can manage your fraud reports by adding, deleting, or editing reports as you get additional information on
    fraudulent users."""

    id: str
    """ID of the associated Beacon Report."""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    type_: BeaconReportTypeOrStr = Field(alias="type")
    """The type of Beacon Report.

    ``first_party``: If this is the same individual as the one who submitted the KYC.

    ``stolen``: If this is a different individual from the one who submitted the KYC.

    ``synthetic``: If this is an individual using fabricated information.

    ``account_takeover``: If this individual's account was compromised.

    ``data_breach``: If this individual's data was compromised in a breach.

    ``unknown``: If you aren't sure who committed the fraud."""

    fraud_date: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    event_date: Date
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    fraud_amount: FraudAmount | None
    """The amount and currency of the fraud or attempted fraud. ``fraud_amount`` should be omitted to indicate an
    unknown fraud amount."""

    audit_trail: BeaconAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BeaconReportCreateResponseDict(TypedDict):
    id: str
    beacon_user_id: str
    created_at: RFC3339DateTime
    type_: BeaconReportTypeOrStr
    fraud_date: Date | None
    event_date: Date
    fraud_amount: FraudAmountDict | None
    audit_trail: BeaconAuditTrailDict
    request_id: str
