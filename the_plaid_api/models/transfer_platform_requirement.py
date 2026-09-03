from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferPlatformRequirement(SdkBaseModel):
    """A piece of information that is required for originator onboarding."""

    requirement_type: Optional[str] = UNSET
    """The type of requirement."""

    person_id: OptionalNullable[str] = UNSET
    """UUID of the person associated with the requirement. Only present for individual-scoped requirements."""


class TransferPlatformRequirementDict(TypedDict):
    requirement_type: NotRequired[str]
    person_id: NotRequired[str | None]
