from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

SandboxTransactionsCreateErrorBody: TypeAlias = Error | None | RawError


@dataclass(frozen=True, slots=True)
class _SandboxTransactionsCreateError:
    def map(self, response: HttpResponse) -> SandboxTransactionsCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Error | None](response)
            case _:
                return RawError(response)


sandbox_transactions_create_error_mapper: Final[
    ErrorMapper[SandboxTransactionsCreateErrorBody]
] = _SandboxTransactionsCreateError()
