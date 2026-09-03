from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeInsightsVersion(str, Enum):
    """The version of Income Insights to use. This value is not shared across API calls for the same resource. If it is
    omitted from a request, the default version is used, even if a version was set in an earlier call such as
    ``/link/token/create`` or ``/cra/check_report/create``."""

    II2 = "II2"

    __str__ = str.__str__


IncomeInsightsVersionOrStr: TypeAlias = Annotated[
    IncomeInsightsVersion | str, open_enum_validator(IncomeInsightsVersion)
]
