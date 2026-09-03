from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.loan_identifier_type import LoanIdentifierTypeOrStr


class LoanIdentifier(SdkBaseModel):
    """The information used to identify this loan by various parties to the transaction or other organizations."""

    loan_identifier: str | None = Field(alias="LoanIdentifier")
    """The value of the identifier for the specified type."""

    loan_identifier_type: LoanIdentifierTypeOrStr | None = Field(alias="LoanIdentifierType")
    """A value from a MISMO prescribed list that specifies the type of loan identifier."""


class LoanIdentifierDict(TypedDict):
    loan_identifier: str | None
    loan_identifier_type: LoanIdentifierTypeOrStr | None
