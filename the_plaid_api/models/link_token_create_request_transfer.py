from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestTransfer(SdkBaseModel):
    """Specifies options for initializing Link for use with the Transfer product."""

    intent_id: Optional[str] = UNSET
    """The ``id`` returned by the ``/transfer/intent/create`` endpoint."""

    authorization_id: Optional[str] = UNSET
    """The ``id`` returned by the ``/transfer/authorization/create`` endpoint. Used to indicate Link session to complete
    required user action in order to make a decision for the authorization. If set, ``access_token`` can be omitted."""

    payment_profile_token: Optional[str] = UNSET
    """The ``payment_profile_token`` returned by the ``/payment_profile/create`` endpoint."""


class LinkTokenCreateRequestTransferDict(TypedDict):
    intent_id: NotRequired[str]
    authorization_id: NotRequired[str]
    payment_profile_token: NotRequired[str]
