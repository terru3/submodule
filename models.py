from pydantic import BaseModel

class Repository(BaseModel):
    repo_name: str
    repo_function: str

class ParentRepository(Repository):
    submodules: list[Repository] = []