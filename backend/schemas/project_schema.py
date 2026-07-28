from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    github_url: Optional[HttpUrl] = None
    language: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    github_url: Optional[str] = None
    language: str
    status: str

    class Config:
        from_attributes = True