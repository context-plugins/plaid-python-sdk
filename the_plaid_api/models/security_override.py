from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SecurityOverride(SdkBaseModel):
    """Specify the security associated with the holding or investment transaction. When inputting custom security data
    to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the
    data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a
    security identifier (``ticker_symbol``, ``cusip``, or ``isin``) are required."""

    isin: Optional[str] = UNSET
    """12-character ISIN, a globally unique securities identifier. A verified CUSIP Global Services license is required
    to receive this data. This field will be null by default for new customers, and null for existing customers starting
    March 12, 2024. If you would like access to this field, please `request ISIN/CUSIP access here
    <https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform>`__."""

    cusip: Optional[str] = UNSET
    """9-character CUSIP, an identifier assigned to North American securities. A verified CUSIP Global Services license
    is required to receive this data. This field will be null by default for new customers, and null for existing
    customers starting March 12, 2024. If you would like access to this field, please `request ISIN/CUSIP access here
    <https://docs.google.com/forms/d/e/1FAIpQLSd9asHEYEfmf8fxJTHZTAfAzW4dugsnSu-HS2J51f1mxwd6Sw/viewform>`__."""

    sedol: Optional[str] = UNSET
    """(Deprecated) 7-character SEDOL, an identifier assigned to securities in the UK."""

    name: Optional[str] = UNSET
    """A descriptive name for the security, suitable for display."""

    ticker_symbol: Optional[str] = UNSET
    """The security's trading symbol for publicly traded securities, and otherwise a short identifier if available."""

    currency: Optional[str] = UNSET
    """Either a valid ``iso_currency_code`` or ``unofficial_currency_code``"""


class SecurityOverrideDict(TypedDict):
    isin: NotRequired[str]
    cusip: NotRequired[str]
    sedol: NotRequired[str]
    name: NotRequired[str]
    ticker_symbol: NotRequired[str]
    currency: NotRequired[str]
