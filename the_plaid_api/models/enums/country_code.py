from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CountryCode(str, Enum):
    """ISO-3166-1 alpha-2 country code standard."""

    US = "US"
    GB = "GB"
    ES = "ES"
    NL = "NL"
    FR = "FR"
    IE = "IE"
    CA = "CA"
    DE = "DE"
    IT = "IT"
    PL = "PL"
    DK = "DK"
    NO = "NO"
    SE = "SE"
    EE = "EE"
    LT = "LT"
    LV = "LV"
    PT = "PT"
    BE = "BE"
    AT = "AT"
    FI = "FI"

    __str__ = str.__str__


CountryCodeOrStr: TypeAlias = Annotated[CountryCode | str, open_enum_validator(CountryCode)]
