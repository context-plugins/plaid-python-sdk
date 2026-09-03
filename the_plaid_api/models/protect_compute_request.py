from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .protect_model_inputs import ProtectModelInputs, ProtectModelInputsDict
from .protect_user import ProtectUser, ProtectUserDict


class ProtectComputeRequest(SdkBaseModel):
    """Request object for /protect/compute"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    model: str
    """The name of the Trust Index model to use for scoring, with a major.minor version suffix. Examples:
    ``ti-link-session-2.0`` (link-session fraud), ``ti-identity-2.0`` (identity fraud), ``cash-advance-onboarding-1.0``
    (first cash advance), and ``cash-advance-ongoing-1.0`` (subsequent cash advances). The model specified may require
    certain fields within ``model_inputs``; for example, ``ti-link-session-2.0`` requires the ``link`` field.
    Cash-advance models do not use ``model_inputs``."""

    user: ProtectUser
    """Represents an end user for ``/protect/compute`` requests."""

    model_inputs: OptionalNullable[ProtectModelInputs] = UNSET
    """Inputs required by certain Trust Index models. The ``link`` field is required for link-session models. Other
    model families (including cash-advance) are identified by ``user`` alone and do not use this object."""


class ProtectComputeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    model: str
    user: ProtectUser | ProtectUserDict
    model_inputs: NotRequired[ProtectModelInputs | ProtectModelInputsDict | None]
