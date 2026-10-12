from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .trust_index_subscore import TrustIndexSubscore, TrustIndexSubscoreDict


class TrustIndexSubscores(SdkBaseModel):
    """Contains sub-score metadata."""

    device_and_connection: OptionalNullable[TrustIndexSubscore] = UNSET
    """Represents Trust Index Subscore."""

    bank_account_insights: OptionalNullable[TrustIndexSubscore] = UNSET
    """Represents Trust Index Subscore."""


class TrustIndexSubscoresDict(TypedDict):
    device_and_connection: NotRequired[TrustIndexSubscoreDict | None]
    bank_account_insights: NotRequired[TrustIndexSubscoreDict | None]
