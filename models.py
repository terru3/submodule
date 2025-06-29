from enum import Enum
from typing import Optional

from pydantic import BaseModel

class Repository(BaseModel):
    repo_name: str
    repo_function: str

class ParentRepository(Repository):
    submodules: list[Repository] = []
    metadata: str

class GitNote(BaseModel):
    concept: str
    explanation: str
    code_example: Optional[str] = None

class GitDiff(BaseModel):
    original: str
    new: str
    submodules: list[Repository] = []

class GitBlame(BaseModel):
    problem: str
    author: str

class GitMergeConflict(BaseModel):
    diff: GitDiff
    blame: GitBlame
    metadata: str
    author: str

class Env(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"
    TEST = "prod"
    CANARY_1 = "canary_1"