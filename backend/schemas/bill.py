from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BillFileData(BaseModel):
    id: int
    title: str
    sponsor_id: int


class Bill(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    id: int
    bill: str
    supporters: int
    opposers: int
    primary_sponsor: Optional[str] = None
