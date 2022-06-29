from typing import Optional
from pydantic import BaseModel


class Aula002Model(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
