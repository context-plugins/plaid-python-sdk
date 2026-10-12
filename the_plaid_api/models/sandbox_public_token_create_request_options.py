from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sandbox_public_token_create_request_options_income_verification import (
    SandboxPublicTokenCreateRequestOptionsIncomeVerification,
    SandboxPublicTokenCreateRequestOptionsIncomeVerificationDict,
)
from .sandbox_public_token_create_request_options_statements import (
    SandboxPublicTokenCreateRequestOptionsStatements,
    SandboxPublicTokenCreateRequestOptionsStatementsDict,
)
from .sandbox_public_token_create_request_options_transactions import (
    SandboxPublicTokenCreateRequestOptionsTransactions,
    SandboxPublicTokenCreateRequestOptionsTransactionsDict,
)


class SandboxPublicTokenCreateRequestOptions(SdkBaseModel):
    """An optional set of options to be used when configuring the Item. If specified, must not be ``null``."""

    webhook: Optional[str] = UNSET
    """Specify a webhook to associate with the new Item."""

    override_username: str | None = "user_good"
    """Test username to use for the creation of the Sandbox Item. Default value is ``user_good``. You can also use a
    custom test user — either set this to the username of a custom user configured in the Dashboard, or set it to
    ``user_custom`` and pass the JSON-stringified custom user configuration object as ``override_password`` to define
    one entirely via API. See `Sandbox Custom Users <https://plaid.com/docs/sandbox/user-custom>`__ for more details."""

    override_password: str | None = "pass_good"
    """Test password to use for the creation of the Sandbox Item. Default value is ``pass_good``. You can also use a
    custom test user — reference one configured in the Dashboard via ``override_username``, or set ``override_username``
    to ``user_custom`` and pass the JSON-stringified custom user configuration object as this field to define one
    entirely via API. See `Sandbox Custom Users <https://plaid.com/docs/sandbox/user-custom>`__ for more details."""

    transactions: OptionalNullable[SandboxPublicTokenCreateRequestOptionsTransactions] = UNSET
    """An optional set of parameters corresponding to transactions options."""

    statements: OptionalNullable[SandboxPublicTokenCreateRequestOptionsStatements] = UNSET
    """An optional set of parameters corresponding to statements options."""

    income_verification: Optional[SandboxPublicTokenCreateRequestOptionsIncomeVerification] = UNSET
    """A set of parameters for income verification options. This field is required if ``income_verification`` is
    included in the ``initial_products`` array."""


class SandboxPublicTokenCreateRequestOptionsDict(TypedDict):
    webhook: NotRequired[str]
    override_username: NotRequired[str | None]
    override_password: NotRequired[str | None]
    transactions: NotRequired[SandboxPublicTokenCreateRequestOptionsTransactionsDict | None]
    statements: NotRequired[SandboxPublicTokenCreateRequestOptionsStatementsDict | None]
    income_verification: NotRequired[SandboxPublicTokenCreateRequestOptionsIncomeVerificationDict]
