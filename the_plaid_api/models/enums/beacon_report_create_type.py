from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BeaconReportCreateType(str, Enum):
    """The type of Beacon Report.

    ``first_party``: If this is the same individual as the one who submitted the KYC.

    ``stolen``: If this is a different individual from the one who submitted the KYC.

    ``synthetic``: If this is an individual using fabricated information.

    ``account_takeover``: If this individual's account was compromised.

    ``unknown``: If you aren't sure who committed the fraud."""

    FIRST_PARTY = "first_party"
    STOLEN = "stolen"
    SYNTHETIC = "synthetic"
    ACCOUNT_TAKEOVER = "account_takeover"
    DATA_BREACH = "data_breach"
    UNKNOWN = "unknown"

    __str__ = str.__str__


BeaconReportCreateTypeOrStr: TypeAlias = Annotated[
    BeaconReportCreateType | str, open_enum_validator(BeaconReportCreateType)
]
