from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerEndCustomerCustomerSupportInfo(SdkBaseModel):
    """This information is public. Users of your app will see this information when managing connections between your
    app and their bank accounts in Plaid Portal. Defaults to partner's customer support info if omitted. This field is
    mandatory for partners whose Plaid accounts were created after November 26, 2024 and will be mandatory for all
    partners by the 1033 compliance deadline."""

    email: Optional[str] = UNSET
    """This field is mandatory for partners whose Plaid accounts were created after November 26, 2024 and will be
    mandatory for all partners by the 1033 compliance deadline."""

    phone_number: Optional[str] = UNSET
    contact_url: Optional[str] = UNSET
    link_update_url: Optional[str] = UNSET


class PartnerEndCustomerCustomerSupportInfoDict(TypedDict):
    email: NotRequired[str]
    phone_number: NotRequired[str]
    contact_url: NotRequired[str]
    link_update_url: NotRequired[str]
