from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UnofficialCurrencyCodeList(str, Enum):
    """List of unofficial currency codes"""

    ADA = "ADA"
    BAT = "BAT"
    BCH = "BCH"
    BNB = "BNB"
    BTC = "BTC"
    BTG = "BTG"
    BSV = "BSV"
    CNH = "CNH"
    DASH = "DASH"
    DOGE = "DOGE"
    ETC = "ETC"
    ETH = "ETH"
    GBX = "GBX"
    LSK = "LSK"
    NEO = "NEO"
    OMG = "OMG"
    QTUM = "QTUM"
    USDT = "USDT"
    XLM = "XLM"
    XMR = "XMR"
    XRP = "XRP"
    ZEC = "ZEC"
    ZRX = "ZRX"

    __str__ = str.__str__


UnofficialCurrencyCodeListOrStr: TypeAlias = Annotated[
    UnofficialCurrencyCodeList | str, open_enum_validator(UnofficialCurrencyCodeList)
]
