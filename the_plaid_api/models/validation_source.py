from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ValidationSource(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    validation_source_name: str | None = Field(alias="ValidationSourceName")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    validation_source_reference_identifier: str | None = Field(alias="ValidationSourceReferenceIdentifier")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class ValidationSourceDict(TypedDict):
    validation_source_name: str | None
    validation_source_reference_identifier: str | None
