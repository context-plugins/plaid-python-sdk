from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.aamvadetailed_match_result import AamvadetailedMatchResultOrStr
from .enums.aamvamatch_result import AamvamatchResultOrStr


class Aamvaanalysis(SdkBaseModel):
    """Analyzed AAMVA data for the associated hit.

    Note: This field is only available for U.S. driver's licenses issued by participating states."""

    is_verified: bool
    """The overall outcome of checking the associated hit against the issuing state database."""

    id_number: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    id_issue_date: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    id_expiration_date: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    street: AamvadetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    city: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    postal_code: AamvadetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    date_of_birth: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    gender: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    height: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    eye_color: AamvamatchResultOrStr
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    first_name: AamvadetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    middle_name: AamvadetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    last_name: AamvadetailedMatchResultOrStr
    """The outcome of checking the associated hit against state databases.


    ``match`` - The field is an exact match with the state database.

    ``partial_match`` - The field is a partial match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""


class AamvaanalysisDict(TypedDict):
    is_verified: bool
    id_number: AamvamatchResultOrStr
    id_issue_date: AamvamatchResultOrStr
    id_expiration_date: AamvamatchResultOrStr
    street: AamvadetailedMatchResultOrStr
    city: AamvamatchResultOrStr
    postal_code: AamvadetailedMatchResultOrStr
    date_of_birth: AamvamatchResultOrStr
    gender: AamvamatchResultOrStr
    height: AamvamatchResultOrStr
    eye_color: AamvamatchResultOrStr
    first_name: AamvadetailedMatchResultOrStr
    middle_name: AamvadetailedMatchResultOrStr
    last_name: AamvadetailedMatchResultOrStr
