from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .taxpayer_identifier import TaxpayerIdentifier, TaxpayerIdentifierDict


class TaxpayerIdentifiers(SdkBaseModel):
    """The collection of ``TAXPAYER_IDENTIFICATION`` elements"""

    taxpayer_identifier: TaxpayerIdentifier = Field(alias="TAXPAYER_IDENTIFIER")
    """Information about the Taxpayer identification values assigned to the individual or legal entity."""


class TaxpayerIdentifiersDict(TypedDict):
    taxpayer_identifier: TaxpayerIdentifierDict
