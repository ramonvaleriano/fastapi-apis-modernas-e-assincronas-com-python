from typing import Optional
from pydantic import BaseModel


class CursosModel(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
