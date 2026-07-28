from pydantic import BaseModel
from typing import List


class FileAnalysis(BaseModel):

    file_name: str

    bugs: List[str]

    security: List[str]

    performance: List[str]

    code_smells: List[str]

    suggestions: List[str]