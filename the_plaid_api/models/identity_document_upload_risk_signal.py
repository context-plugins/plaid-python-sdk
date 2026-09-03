from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IdentityDocumentUploadRiskSignal(SdkBaseModel):
    """Risk signals tied to the document"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of risk found."""

    has_fraud_risk: OptionalNullable[bool] = UNSET
    """Indicates whether fraud risk was detected for this risk signal."""

    signal_description: OptionalNullable[str] = UNSET
    """A human-readable explanation providing more detail about the specific risk signal."""

    page_number: OptionalNullable[int] = UNSET
    """The relevant page associated with the risk signal. If the risk signal is not associated with a specific page, the
    value will be 0."""


class IdentityDocumentUploadRiskSignalDict(TypedDict):
    type_: NotRequired[str | None]
    has_fraud_risk: NotRequired[bool | None]
    signal_description: NotRequired[str | None]
    page_number: NotRequired[int | None]
