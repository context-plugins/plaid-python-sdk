from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ProductAccess(SdkBaseModel):
    """The product access being requested. Used to allow or disallow product access across all accounts. If unset,
    defaults to all products allowed."""

    statements: OptionalNullable[bool] = UNSET
    """Allow access to statements. Only used by certain partners. If relevant to the partner and unset, defaults to
    ``true``."""

    identity: OptionalNullable[bool] = UNSET
    """Allow access to the Identity product (name, email, phone, address). Only used by certain partners. If relevant to
    the partner and unset, defaults to ``true``."""

    auth: OptionalNullable[bool] = UNSET
    """Allow access to account number details. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""

    transactions: OptionalNullable[bool] = UNSET
    """Allow access to transaction details. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""

    accounts_details_transactions: OptionalNullable[bool] = UNSET
    """Allow access to ``accounts_details_transactions``. Only used by certain partners. If relevant to the partner and
    unset, defaults to ``true``."""

    accounts_routing_number: OptionalNullable[bool] = UNSET
    """Allow access to ``accounts_routing_number``. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""

    accounts_statements: OptionalNullable[bool] = UNSET
    """Allow access to ``accounts_statements``. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""

    accounts_tax_statements: OptionalNullable[bool] = UNSET
    """Allow access to ``accounts_tax_statements``. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""

    customers_profiles: OptionalNullable[bool] = UNSET
    """Allow access to ``customers_profiles``. Only used by certain partners. If relevant to the partner and unset,
    defaults to ``true``."""


class ProductAccessDict(TypedDict):
    statements: NotRequired[bool | None]
    identity: NotRequired[bool | None]
    auth: NotRequired[bool | None]
    transactions: NotRequired[bool | None]
    accounts_details_transactions: NotRequired[bool | None]
    accounts_routing_number: NotRequired[bool | None]
    accounts_statements: NotRequired[bool | None]
    accounts_tax_statements: NotRequired[bool | None]
    customers_profiles: NotRequired[bool | None]
