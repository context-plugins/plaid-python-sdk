from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LinkTokenInvestmentsAuth(SdkBaseModel):
    """Configuration parameters for the Investments Move product"""

    manual_entry_enabled: bool | None = False
    """If ``true``, show institutions that use the manual entry fallback flow."""

    masked_number_match_enabled: bool | None = False
    """If ``true``, show institutions that use the masked number match fallback flow."""

    stated_account_number_enabled: bool | None = False
    """If ``true``, show institutions that use the stated account number fallback flow."""

    rollover_401k_enabled: bool | None = False
    """If ``true``, the fee and contribution details for 401k accounts will be returned."""


class LinkTokenInvestmentsAuthDict(TypedDict):
    manual_entry_enabled: NotRequired[bool | None]
    masked_number_match_enabled: NotRequired[bool | None]
    stated_account_number_enabled: NotRequired[bool | None]
    rollover_401k_enabled: NotRequired[bool | None]
