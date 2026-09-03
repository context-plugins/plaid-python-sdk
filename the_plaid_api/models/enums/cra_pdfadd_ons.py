from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraPdfaddOns(str, Enum):
    """A list of add-ons that can be included in the PDF.

    ``cra_income_insights``: Include Income Insights report in the PDF. ``cra_partner_insights``: Include Partner
    Insights report in the PDF."""

    CRA_INCOME_INSIGHTS = "cra_income_insights"
    CRA_PARTNER_INSIGHTS = "cra_partner_insights"

    __str__ = str.__str__


CraPdfaddOnsOrStr: TypeAlias = Annotated[CraPdfaddOns | str, open_enum_validator(CraPdfaddOns)]
