from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .consented_account import ConsentedAccount, ConsentedAccountDict
from .enums.consent_event_code import ConsentEventCodeOrStr
from .enums.consent_event_initiator import ConsentEventInitiatorOrStr
from .enums.consent_event_type import ConsentEventTypeOrStr


class ConsentEvent(SdkBaseModel):
    """Describes a consent event."""

    item_id: Optional[str] = UNSET
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """The date and time when the consent event occurred, in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__
    format."""

    event_type: Optional[ConsentEventTypeOrStr] = UNSET
    """A broad categorization of the consent event."""

    event_code: Optional[ConsentEventCodeOrStr] = UNSET
    """Codes describing the object of a consent event."""

    institution_id: OptionalNullable[str] = UNSET
    """Unique identifier for the institution associated with the Item. Field is ``null`` for Items created via Same-Day
    Micro-deposits."""

    institution_name: OptionalNullable[str] = UNSET
    """The full name of the institution associated with the Item. Field is ``null`` for Items created via Same-Day
    Micro-deposits."""

    initiator: Optional[ConsentEventInitiatorOrStr] = UNSET
    """The entity that initiated collection of consent."""

    consented_use_cases: Optional[list[str]] = UNSET
    """A list of strings containing the full list of use cases the end user has consented to for the Item.

    See the `full list
    <https://plaid.com/docs/link/data-transparency-messaging-migration-guide/#updating-link-customizations>`__ of use
    cases."""

    consented_data_scopes: Optional[list[str]] = UNSET
    """A list of strings containing the full list of data scopes the end user has consented to for the Item. These
    correspond to consented products; see the `full mapping
    <https://plaid.com/docs/link/data-transparency-messaging-migration-guide/#data-scopes-by-product>`__ of data scopes
    and products."""

    consented_accounts: Optional[list[ConsentedAccount]] = UNSET
    """An array containing the accounts associated with the Item for which authorizations are granted."""


class ConsentEventDict(TypedDict):
    item_id: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    event_type: NotRequired[ConsentEventTypeOrStr]
    event_code: NotRequired[ConsentEventCodeOrStr]
    institution_id: NotRequired[str | None]
    institution_name: NotRequired[str | None]
    initiator: NotRequired[ConsentEventInitiatorOrStr]
    consented_use_cases: NotRequired[list[str]]
    consented_data_scopes: NotRequired[list[str]]
    consented_accounts: NotRequired[list[ConsentedAccountDict]]
