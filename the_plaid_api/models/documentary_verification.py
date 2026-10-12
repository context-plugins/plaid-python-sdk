from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .documentary_verification_document import DocumentaryVerificationDocument, DocumentaryVerificationDocumentDict


class DocumentaryVerification(SdkBaseModel):
    """Data, images, analysis, and results from the ``documentary_verification`` step. This field will be ``null``
    unless ``steps.documentary_verification`` has reached a terminal state of either ``success`` or ``failed``."""

    status: str
    """The outcome status for the associated Identity Verification attempt's ``documentary_verification`` step. This
    field will always have the same value as ``steps.documentary_verification``."""

    documents: list[DocumentaryVerificationDocument]
    """An array of documents submitted to the ``documentary_verification`` step. Each entry represents one user
    submission, where each submission will contain both a front and back image, or just a front image, depending on the
    document type.

    Note: Plaid will automatically let a user submit a new set of document images up to three times if we detect that a
    previous attempt might have failed due to user error. For example, if the first set of document images are blurry or
    obscured by glare, the user will be asked to capture their documents again, resulting in at least two separate
    entries within ``documents``. If the overall ``documentary_verification`` is ``failed``, the user has exhausted
    their retry attempts."""


class DocumentaryVerificationDict(TypedDict):
    status: str
    documents: list[DocumentaryVerificationDocumentDict]
