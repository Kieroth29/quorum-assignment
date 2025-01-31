from enum import IntEnum

from pydantic import BaseModel


class Vote(BaseModel):
    id: int
    bill_id: int


class VoteTypeEnum(IntEnum):
    SUPPORT = 1
    OPPOSE = 2


class VoteResult(BaseModel):
    id: int
    legislator_id: int
    vote_id: int
    vote_type: VoteTypeEnum
