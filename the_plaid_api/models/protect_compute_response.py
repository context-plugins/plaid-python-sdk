from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .protect_compute_subscores import ProtectComputeSubscores, ProtectComputeSubscoresDict


class ProtectComputeResponse(SdkBaseModel):
    """Response object for /protect/compute"""

    score: OptionalNullable[int] = UNSET
    """The Trust Index score, on a 0-100 scale where higher values indicate lower risk."""

    model: Optional[str] = UNSET
    """The versioned name of the Trust Index model used for scoring."""

    attributes: OptionalNullable[Any] = UNSET
    """Event fraud attributes as an arbitrary set of key-value pairs. The set of attributes returned varies by model."""

    subscores: OptionalNullable[ProtectComputeSubscores] = UNSET
    """Per-bucket subscores returned alongside the overall Trust Index score. For cash-advance models, each key maps to
    an amount-bucket subscore (0-100); higher values indicate lower fraud risk. Only buckets that were scored are
    included in the response."""

    timestamp: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp when the Trust Index score and fraud attributes were computed, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g. ``"2017-09-14T14:42:19.350Z"``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProtectComputeResponseDict(TypedDict):
    score: NotRequired[int | None]
    model: NotRequired[str]
    attributes: NotRequired[Any | None]
    subscores: NotRequired[ProtectComputeSubscoresDict | None]
    timestamp: NotRequired[RFC3339DateTime | None]
    request_id: str
