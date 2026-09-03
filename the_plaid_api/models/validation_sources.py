from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .validation_source import ValidationSource, ValidationSourceDict


class ValidationSources(SdkBaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    validation_source: list[ValidationSource] = Field(alias="VALIDATION_SOURCE")
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


class ValidationSourcesDict(TypedDict):
    validation_source: list[ValidationSource | ValidationSourceDict]
