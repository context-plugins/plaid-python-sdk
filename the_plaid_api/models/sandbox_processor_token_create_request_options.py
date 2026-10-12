from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SandboxProcessorTokenCreateRequestOptions(SdkBaseModel):
    """An optional set of options to be used when configuring the Item. If specified, must not be ``null``."""

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


class SandboxProcessorTokenCreateRequestOptionsDict(TypedDict):
    override_username: NotRequired[str | None]
    override_password: NotRequired[str | None]
