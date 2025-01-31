from pathlib import Path

from typing import Dict, List, TypeAlias, Union

import pandas as pd

from schemas.votes import Vote, VoteResult
from schemas.bill import BillFileData
from schemas.legislator import LegislatorFileData

BillData: TypeAlias = List[BillFileData]
LegislatorData: TypeAlias = List[LegislatorFileData]
VoteResultData: TypeAlias = List[VoteResult]
VoteData: TypeAlias = List[Vote]


def build_file_path(file: str) -> str:
    """Build file path to data directory based on file name."""
    return Path(__file__).parent / f'../data/{file}'


def import_bills() -> List[BillFileData]:
    """Import bills data from .csv file and return list of Pydantic class objects."""
    df = pd.read_csv(build_file_path('bills_(2).csv'))

    return [BillFileData(**row) for row in df.to_dict('index').values()]


def import_legislators() -> List[LegislatorFileData]:
    """Import legislators data from .csv file and return list of Pydantic class objects."""
    df = pd.read_csv(build_file_path('legislators_(2).csv'))

    return [LegislatorFileData(**row) for row in df.to_dict('index').values()]


def import_vote_results() -> List[VoteResult]:
    """Import vote results data from .csv file and return list of Pydantic class objects."""
    df = pd.read_csv(build_file_path('vote_results_(2).csv'))
    return [VoteResult(**row) for row in df.to_dict('index').values()]


def import_votes() -> List[Vote]:
    """Import votes data from .csv file and return list of Pydantic class objects."""
    df = pd.read_csv(build_file_path('votes_(2).csv'))
    return [Vote(**row) for row in df.to_dict('index').values()]


def import_data() -> Dict[str, Union[BillData, LegislatorData, VoteResultData, VoteData]]:
    """Import all data from .csv files and return a dictionary with Pydantic class objects for each context."""
    return {
        'bills': import_bills(),
        'legislators': import_legislators(),
        'vote_results': import_vote_results(),
        'votes': import_votes()
    }
