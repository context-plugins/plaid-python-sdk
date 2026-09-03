from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCheckReportPermissiblePurpose(str, Enum):
    """The permissible purpose under the FCRA for retrieving this consumer report. Restricted to permissible purposes
    related to loan servicing only. Required when ``report_id`` is provided."""

    ACCOUNT_REVIEW_CREDIT = "ACCOUNT_REVIEW_CREDIT"
    WRITTEN_INSTRUCTION_OTHER = "WRITTEN_INSTRUCTION_OTHER"

    __str__ = str.__str__


CraCheckReportPermissiblePurposeOrStr: TypeAlias = Annotated[
    CraCheckReportPermissiblePurpose | str, open_enum_validator(CraCheckReportPermissiblePurpose)
]
