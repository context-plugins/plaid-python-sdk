from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.fraud_check_outcome import FraudCheckOutcomeOrStr
from .enums.fraud_check_outcome_with_no_data import FraudCheckOutcomeWithNoDataOrStr


class FraudAnalysisDetails(SdkBaseModel):
    """Details about the fraud analysis performed on the document."""

    type_supported: FraudCheckOutcomeOrStr
    """Whether the submitted document type is supported for fraud analysis.

    ``success`` - The document type is supported.

    ``failed`` - The document type is not supported."""

    portrait_presence_check: FraudCheckOutcomeOrStr
    """The outcome of the portrait presence check.

    ``success`` - A portrait was detected.

    ``failed`` - No portrait was detected."""

    portrait_details_check: FraudCheckOutcomeOrStr
    """The outcome of the portrait details check including photo embedding and face landmark checks.

    ``success`` - The portrait passed all validity checks.

    ``failed`` - The portrait did not pass one or more validity checks."""

    image_composition_check: FraudCheckOutcomeOrStr
    """The outcome of the image composition check.

    ``success`` - The image is a valid physical document capture.

    ``failed`` - The image appears to be a photograph of a screen or a digital forgery."""

    integrity_check: FraudCheckOutcomeOrStr
    """The outcome of the integrity check for document security elements.

    ``success`` - Data is consistent across all checked security elements.

    ``failed`` - Inconsistencies were detected across one or more security elements."""

    detail_check: FraudCheckOutcomeOrStr
    """The outcome of the document detail check for correct styling and layout.

    ``success`` - The document passed all authenticity checks.

    ``failed`` - The document did not pass one or more authenticity checks."""

    issue_date_check: FraudCheckOutcomeWithNoDataOrStr
    """The outcome of the issue date validity check.

    ``success`` - The issue date is valid.

    ``failed`` - The issue date is invalid or could not be verified.

    ``no_data`` - The check could not be performed due to insufficient data."""


class FraudAnalysisDetailsDict(TypedDict):
    type_supported: FraudCheckOutcomeOrStr
    portrait_presence_check: FraudCheckOutcomeOrStr
    portrait_details_check: FraudCheckOutcomeOrStr
    image_composition_check: FraudCheckOutcomeOrStr
    integrity_check: FraudCheckOutcomeOrStr
    detail_check: FraudCheckOutcomeOrStr
    issue_date_check: FraudCheckOutcomeWithNoDataOrStr
