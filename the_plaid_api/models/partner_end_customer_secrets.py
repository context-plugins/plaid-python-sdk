from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerEndCustomerSecrets(SdkBaseModel):
    """The secrets for the newly created end customer."""

    sandbox: Optional[str] = UNSET
    """The end customer's secret key for the Sandbox environment."""

    development: Optional[str] = UNSET
    """The end customer's secret key for the Development environment. The Development environment has been removed."""

    production: Optional[str] = UNSET
    """The end customer's secret key for the Production environment. The end customer will be provided with a limited
    number of credits to test in the Production environment before full enablement."""


class PartnerEndCustomerSecretsDict(TypedDict):
    sandbox: NotRequired[str]
    development: NotRequired[str]
    production: NotRequired[str]
