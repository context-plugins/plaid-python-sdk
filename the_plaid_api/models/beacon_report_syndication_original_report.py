from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, RFC3339DateTime, SdkBaseModel
from .enums.beacon_report_type import BeaconReportTypeOrStr


class BeaconReportSyndicationOriginalReport(SdkBaseModel):
    """A subset of information from a Beacon Report that has been syndicated to a matching Beacon User in your program.

    The ``id`` field in the response is the ID of the original report that was syndicated. If the original report was
    created by your organization, the field will be filled with the ID of the report. Otherwise, the field will be
    ``null`` indicating that the original report was created by another Beacon customer."""

    id: str | None
    """ID of the associated Beacon Report."""

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


class BeaconReportSyndicationOriginalReportDict(TypedDict):
    id: str | None
    created_at: RFC3339DateTime
    type_: BeaconReportTypeOrStr
    fraud_date: Date | None
    event_date: Date
