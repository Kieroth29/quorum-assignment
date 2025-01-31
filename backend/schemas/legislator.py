from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class LegislatorFileData(BaseModel):
    id: int
    name: str


class Legislator(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    id: int
    legislator: str
    supported_bills: int
    opposed_bills: int
