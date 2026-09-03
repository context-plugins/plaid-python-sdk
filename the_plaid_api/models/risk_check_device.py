from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.proxy_type import ProxyTypeOrStr
from .enums.risk_level import RiskLevelOrStr


class RiskCheckDevice(SdkBaseModel):
    """Result summary object specifying values for ``device`` attributes of risk check."""

    ip_proxy_type: ProxyTypeOrStr | None
    """An enum indicating whether a network proxy is present and if so what type it is.

    ``none_detected`` indicates the user is not on a detectable proxy network.

    ``tor`` indicates the user was using a Tor browser, which sends encrypted traffic on a decentralized network and is
    somewhat similar to a VPN (Virtual Private Network).

    ``vpn`` indicates the user is on a VPN (Virtual Private Network)

    ``web_proxy`` indicates the user is on a web proxy server, which may allow them to conceal information such as their
    IP address or other identifying information.

    ``public_proxy`` indicates the user is on a public web proxy server, which is similar to a web proxy but can be
    shared by multiple users. This may allow multiple users to appear as if they have the same IP address for
    instance."""

    ip_spam_list_count: int | None
    """Count of spam lists the IP address is associated with if known."""

    ip_timezone_offset: str | None
    """UTC offset of the timezone associated with the IP address."""

    risk_level: Optional[RiskLevelOrStr] = UNSET
    """Risk level for the given risk check type."""

    factors: Optional[list[str]] = UNSET
    """List of factors, when available, that contribute towards the risk level of the given risk check type."""


class RiskCheckDeviceDict(TypedDict):
    ip_proxy_type: ProxyTypeOrStr | None
    ip_spam_list_count: int | None
    ip_timezone_offset: str | None
    risk_level: NotRequired[RiskLevelOrStr]
    factors: NotRequired[list[str]]
