from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .protect_link_model_inputs import ProtectLinkModelInputs, ProtectLinkModelInputsDict
from .protect_sdkmodel_inputs import ProtectSdkmodelInputs, ProtectSdkmodelInputsDict


class ProtectModelInputs(SdkBaseModel):
    """Inputs required by certain Trust Index models. The ``link`` field is required for link-session models. Other
    model families (including cash-advance) are identified by ``user`` alone and do not use this object."""

    link: OptionalNullable[ProtectLinkModelInputs] = UNSET
    """Inputs for link session Trust Index models."""

    sdk: OptionalNullable[ProtectSdkmodelInputs] = UNSET
    """Inputs for Protect SDK Trust Index models."""


class ProtectModelInputsDict(TypedDict):
    link: NotRequired[ProtectLinkModelInputsDict | None]
    sdk: NotRequired[ProtectSdkmodelInputsDict | None]
