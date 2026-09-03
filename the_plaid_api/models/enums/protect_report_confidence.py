from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProtectReportConfidence(str, Enum):
    """The confidence level of the incident report. ``CONFIRMED`` indicates the incident has been verified and
    definitively occurred.

    ``SUSPECTED`` indicates the incident is believed to have occurred but has not been fully verified."""

    CONFIRMED = "CONFIRMED"
    SUSPECTED = "SUSPECTED"

    __str__ = str.__str__


ProtectReportConfidenceOrStr: TypeAlias = Annotated[
    ProtectReportConfidence | str, open_enum_validator(ProtectReportConfidence)
]
