from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cra_employment_refresh_report import CraEmploymentRefreshReport, CraEmploymentRefreshReportDict
from .cra_verification_income_report import CraVerificationIncomeReport, CraVerificationIncomeReportDict
from .cra_voa_report import CraVoaReport, CraVoaReportDict


class CraVerificationReport(SdkBaseModel):
    """Contains data for the CRA Home Lending Report."""

    report_id: str
    """The unique identifier associated with the Home Lending Report object. This ID will be the same as the Base Report
    ID."""

    gse_reference_id: Optional[str] = UNSET
    """A unique token that can be shared with GSEs in order to provide them access to the report. This is automatically
    created during report generation when GSE options are specified."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    voa: OptionalNullable[CraVoaReport] = UNSET
    """An object representing a VOA report."""

    employment_refresh: OptionalNullable[CraEmploymentRefreshReport] = UNSET
    """An object representing an Employment Refresh Report."""

    income: OptionalNullable[CraVerificationIncomeReport] = UNSET
    """An object representing an Income Report within the Home Lending Report."""


class CraVerificationReportDict(TypedDict):
    report_id: str
    gse_reference_id: NotRequired[str]
    client_report_id: NotRequired[str | None]
    voa: NotRequired[CraVoaReportDict | None]
    employment_refresh: NotRequired[CraEmploymentRefreshReportDict | None]
    income: NotRequired[CraVerificationIncomeReportDict | None]
