from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemAuthMethod(str, Enum):
    """The method used to populate Auth data for the Item. This field is only populated for Items that have had Auth
    numbers data set on at least one of their accounts, and will be ``null`` otherwise. For info about the various
    flows, see our `Auth coverage documentation <https://plaid.com/docs/auth/coverage/>`__.

    ``INSTANT_AUTH``: The Item's Auth data was provided directly by the user's institution connection.

    ``INSTANT_MATCH``: The Item's Auth data was provided via the Instant Match fallback flow.

    ``AUTOMATED_MICRODEPOSITS``: The Item's Auth data was provided via the Automated Micro-deposits flow.

    ``SAME_DAY_MICRODEPOSITS``: The Item's Auth data was provided via the Same-Day Micro-deposits flow.

    ``INSTANT_MICRODEPOSITS``: The Item's Auth data was provided via the Instant Micro-deposits flow.

    ``DATABASE_MATCH``: The Item's Auth data was provided via the Database Match flow.

    ``DATABASE_INSIGHTS``: The Item's Auth data was provided via the Database Insights flow.

    ``TRANSFER_MIGRATED``: The Item's Auth data was provided via
    https://plaid.com/docs/api/products/transfer/account-linking/#migrate-account-into-transfers.

    ``INVESTMENTS_FALLBACK``: The Item's Auth data for Investments Move was provided via a `fallback flow
    <https://plaid.com/docs/investments-move/#fallback-flows>`__."""

    INSTANT_AUTH = "INSTANT_AUTH"
    INSTANT_MATCH = "INSTANT_MATCH"
    AUTOMATED_MICRODEPOSITS = "AUTOMATED_MICRODEPOSITS"
    SAME_DAY_MICRODEPOSITS = "SAME_DAY_MICRODEPOSITS"
    INSTANT_MICRODEPOSITS = "INSTANT_MICRODEPOSITS"
    DATABASE_MATCH = "DATABASE_MATCH"
    DATABASE_INSIGHTS = "DATABASE_INSIGHTS"
    TRANSFER_MIGRATED = "TRANSFER_MIGRATED"
    INVESTMENTS_FALLBACK = "INVESTMENTS_FALLBACK"

    __str__ = str.__str__


ItemAuthMethodOrStr: TypeAlias = Annotated[ItemAuthMethod | str, open_enum_validator(ItemAuthMethod)]
