<<<<<<< HEAD
from typing import Optional

=======
>>>>>>> e6e9845 (add pydantic model dummy and gitignore)
from pydantic import BaseModel

class Repository(BaseModel):
    repo_name: str
    repo_function: str

class ParentRepository(Repository):
<<<<<<< HEAD
    submodules: list[Repository] = []

class GitNote(BaseModel):
    concept: str
    explanation: str
    code_example: Optional[str] = None

class GitDiff(BaseModel):
    original: str
    new: str
=======
    submodules: list[Repository] = []
>>>>>>> e6e9845 (add pydantic model dummy and gitignore)
