from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit_document_metadata import CreditDocumentMetadata, CreditDocumentMetadataDict
from .credit_i20_student import CreditI20Student, CreditI20StudentDict


class CreditI20(SdkBaseModel):
    """An object representing an end user's Form I-20 US immigration student document."""

    document_id: OptionalNullable[str] = UNSET
    """An identifier of the document referenced by the document metadata."""

    document_metadata: Optional[CreditDocumentMetadata] = UNSET
    """Object representing metadata pertaining to the document."""

    student: Optional[CreditI20Student] = UNSET
    """An object representing the student named on a Form I-20."""

    personal_funds: OptionalNullable[float] = UNSET
    """Amount of the student's personal funds."""

    on_campus_employment: OptionalNullable[float] = UNSET
    """Amount of funds from on-campus employment."""

    funds_from_this_school: OptionalNullable[float] = UNSET
    """Amount of funds provided by the issuing school."""

    students_funding_total: OptionalNullable[float] = UNSET
    """Total amount of funds available to the student."""

    funds_from_another_source: OptionalNullable[float] = UNSET
    """Amount of funds from another source."""

    estimated_average_costs_total: OptionalNullable[float] = UNSET
    """Estimated total average costs for the program period."""

    estimated_average_living_expenses: OptionalNullable[float] = UNSET
    """Estimated average living expenses."""

    students_funding_period_months: OptionalNullable[int] = UNSET
    """Number of months the student's funding covers."""

    estimated_average_costs_period_months: OptionalNullable[int] = UNSET
    """Number of months the estimated average costs cover."""


class CreditI20Dict(TypedDict):
    document_id: NotRequired[str | None]
    document_metadata: NotRequired[CreditDocumentMetadata | CreditDocumentMetadataDict]
    student: NotRequired[CreditI20Student | CreditI20StudentDict]
    personal_funds: NotRequired[float | None]
    on_campus_employment: NotRequired[float | None]
    funds_from_this_school: NotRequired[float | None]
    students_funding_total: NotRequired[float | None]
    funds_from_another_source: NotRequired[float | None]
    estimated_average_costs_total: NotRequired[float | None]
    estimated_average_living_expenses: NotRequired[float | None]
    students_funding_period_months: NotRequired[int | None]
    estimated_average_costs_period_months: NotRequired[int | None]
