from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.taxpayer_identifier_type import TaxpayerIdentifierTypeOrStr


class TaxpayerIdentifier(SdkBaseModel):
    """Information about the Taxpayer identification values assigned to the individual or legal entity."""

    taxpayer_identifier_type: TaxpayerIdentifierTypeOrStr | None = Field(alias="TaxpayerIdentifierType")
    """A value from a MISMO prescribed list that classifies identification numbers used by the Internal Revenue Service
    (IRS) in the administration of tax laws. A Social Security number (SSN) is issued by the SSA; all other taxpayer
    identification numbers are issued by the IRS."""

    taxpayer_identifier_value: str | None = Field(alias="TaxpayerIdentifierValue")
    """The value of the taxpayer identifier as assigned by the IRS to the individual or legal entity."""


class TaxpayerIdentifierDict(TypedDict):
    taxpayer_identifier_type: TaxpayerIdentifierTypeOrStr | None
    taxpayer_identifier_value: str | None
