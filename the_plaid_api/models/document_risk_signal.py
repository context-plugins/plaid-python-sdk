from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .document_risk_signal_institution_metadata import (
    DocumentRiskSignalInstitutionMetadata,
    DocumentRiskSignalInstitutionMetadataDict,
)


class DocumentRiskSignal(SdkBaseModel):
    """Details about a certain reason as to why a document could potentially be fraudulent."""

    type_: str | None = Field(alias="type")
    """The type of risk found in the risk signal check."""

    field: str | None
    """The field which the risk signal was computed for"""

    has_fraud_risk: bool | None
    """A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent"""

    institution_metadata: DocumentRiskSignalInstitutionMetadata | None
    """An object which contains additional metadata about the institution used to compute the verification attribute"""

    expected_value: str | None
    """The expected value of the field, as seen on the document"""

    actual_value: str | None
    """The derived value obtained in the risk signal calculation process for this field"""

    signal_description: str | None
    """A human-readable explanation providing more detail into the particular risk signal"""

    page_number: int | None
    """The relevant page associated with the risk signal. If the risk signal is not associated with a specific page, the
    value will be 0."""


class DocumentRiskSignalDict(TypedDict):
    type_: str | None
    field: str | None
    has_fraud_risk: bool | None
    institution_metadata: DocumentRiskSignalInstitutionMetadata | DocumentRiskSignalInstitutionMetadataDict | None
    expected_value: str | None
    actual_value: str | None
    signal_description: str | None
    page_number: int | None
