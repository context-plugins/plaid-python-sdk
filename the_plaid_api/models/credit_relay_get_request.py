from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditRelayGetRequest(SdkBaseModel):
    """CreditRelayGetRequest defines the request schema for ``/credit/relay/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    relay_token: str
    """The ``relay_token`` granting access to the report you would like to get."""

    report_type: Literal["asset"] = "asset"
    """The report type. It can be ``asset``. Income report types are not yet supported."""

    include_insights: Optional[bool] = UNSET
    """``true`` if you would like to retrieve the Asset Report with Insights, ``false`` otherwise. This field defaults
    to ``false`` if omitted."""


class CreditRelayGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    relay_token: str
    report_type: NotRequired[Literal["asset"]]
    include_insights: NotRequired[bool]
