from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PayrollItemStatus(SdkBaseModel):
    """Details about the status of the payroll item."""

    processing_status: OptionalNullable[str] = UNSET
    """Denotes the processing status for the verification.

    ``UNKNOWN``: The processing status could not be determined.

    ``PROCESSING_COMPLETE``: The processing has completed and the user has approved for sharing. The data is available
    to be retrieved.

    ``PROCESSING``: The verification is still processing. The data is not available yet.

    ``FAILED``: The processing failed to complete successfully.

    ``APPROVAL_STATUS_PENDING``: The processing has completed but the user has not yet approved the sharing of the
    data."""


class PayrollItemStatusDict(TypedDict):
    processing_status: NotRequired[str | None]
