from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.aamva_detailed_match_result import AamvaDetailedMatchResultOrStr
from .enums.aamva_match_result import AamvaMatchResultOrStr


class AamvaAnalysis(SdkBaseModel):
    """Analyzed AAMVA data for the associated hit.

    Note: This field is only available for U.S. driver's licenses issued by participating states."""

    is_verified: bool
    """The overall outcome of checking the associated hit against the issuing state database."""

    id_number: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    id_issue_date: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    id_expiration_date: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    street: AamvaDetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    city: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    postal_code: AamvaDetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    date_of_birth: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    gender: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    height: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    eye_color: AamvaMatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    first_name: AamvaDetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    middle_name: AamvaDetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    last_name: AamvaDetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""


class AamvaAnalysisDict(TypedDict):
    is_verified: bool
    id_number: AamvaMatchResultOrStr
    id_issue_date: AamvaMatchResultOrStr
    id_expiration_date: AamvaMatchResultOrStr
    street: AamvaDetailedMatchResultOrStr
    city: AamvaMatchResultOrStr
    postal_code: AamvaDetailedMatchResultOrStr
    date_of_birth: AamvaMatchResultOrStr
    gender: AamvaMatchResultOrStr
    height: AamvaMatchResultOrStr
    eye_color: AamvaMatchResultOrStr
    first_name: AamvaDetailedMatchResultOrStr
    middle_name: AamvaDetailedMatchResultOrStr
    last_name: AamvaDetailedMatchResultOrStr
