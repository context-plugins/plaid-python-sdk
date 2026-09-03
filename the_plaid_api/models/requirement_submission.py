from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RequirementSubmission(SdkBaseModel):
    """A single requirement submission"""

    requirement_type: str
    """The type of requirement being submitted. See `Requirement type schema documentation
    <https://docs.google.com/document/d/1NEQkTD0sVK50iAQi6xHigrexDUxZ4QxXqSEfV_FFTiU/>`__ for a list of requirement
    types and possible values."""

    value: str
    """The value of the requirement, which can be a string or an object depending on the ``requirement_type``. If it is
    an object, the object should be JSON marshaled into a string. See `Requirement type schema documentation
    <https://docs.google.com/document/d/1NEQkTD0sVK50iAQi6xHigrexDUxZ4QxXqSEfV_FFTiU/>`__ for a list of requirement
    types and possible values."""

    person_id: Optional[UUID] = UNSET
    """The ``person_id`` of the person the requirement submission is related to. A ``person_id`` is returned by
    ``/transfer/platform/person/create``. This field should not be included for requirements that are not related to a
    person."""


class RequirementSubmissionDict(TypedDict):
    requirement_type: str
    value: str
    person_id: NotRequired[UUID]
