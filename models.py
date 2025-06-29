from typing import Optional

from pydantic import BaseModel

class Repository(BaseModel):
    repo_name: str
    repo_function: str

class ParentRepository(Repository):
    submodules: list[Repository] = []

class GitNote(BaseModel):
    concept: str
    explanation: str
    code_example: Optional[str] = None

class GitDiff(BaseModel):
    original: str
    new: str