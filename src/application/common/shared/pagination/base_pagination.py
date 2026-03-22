from pydantic import BaseModel, Field


class BasePagination(BaseModel):
    limit: int = Field(0, gt=10)
    offset: int = Field(0, gt=0)
