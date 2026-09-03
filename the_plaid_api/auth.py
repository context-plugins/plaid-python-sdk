from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    client_id: AuthScheme
    secret: AuthScheme
    plaid_version: AuthScheme
    oauth2: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    client_id: AsyncAuthScheme
    secret: AsyncAuthScheme
    plaid_version: AsyncAuthScheme
    oauth2: AsyncAuthScheme


Oauth2Scope: TypeAlias = Literal["cra:report:read", "user:write"]
"""``cra:report:read``: Read CRA report data. ``user:write``: Write user data."""
