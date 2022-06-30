from typing import Optional
from pydantic import BaseModel, validator


class CursosModel(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ver pelo menos 3 palavras')

        if value.islower():

            raise ValueError('O titulo não pode ser todo minusculo')

        return value

    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value <= 0:
            raise ValueError('Por favor, apenas número positivos')
        if value < 12:
            raise ValueError('O número do aulas tem que ser maior que 12')

        return value

    @validator('horas')
    def validar_hotas(cls, value: int):
        if value <= 0:
            raise ValueError('Por favor, apenas número positivos')
        if value < 10:
            raise ValueError('O número do horas tem que ser mais que 10 horas')

        return value
