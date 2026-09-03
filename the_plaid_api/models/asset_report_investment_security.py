from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetReportInvestmentSecurity(SdkBaseModel):
    """Investment security associated with the account."""

    security_id: str
    """A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid
    identifiers, the ``security_id`` is case sensitive. The ``security_id`` may change if inherent details of the
    security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change."""

    name: str | None
    """A descriptive name for the security, suitable for display."""

    ticker_symbol: str | None
    """The security's trading symbol for publicly traded securities, and otherwise a short identifier if available."""

    type_: str | None = Field(alias="type")
    """The security type of the holding. Valid security types are:

    ``cash``: Cash, currency, and money market funds

    ``cryptocurrency``: Digital or virtual currencies

    ``derivative``: Options, warrants, and other derivative instruments

    ``equity``: Domestic and foreign equities

    ``etf``: Multi-asset exchange-traded investment funds

    ``fixed income``: Bonds and certificates of deposit (CDs)

    ``loan``: Loans and loan receivables

    ``mutual fund``: Open- and closed-end vehicles pooling funds of multiple investors

    ``other``: Unknown or other investment types"""


class AssetReportInvestmentSecurityDict(TypedDict):
    security_id: str
    name: str | None
    ticker_symbol: str | None
    type_: str | None
