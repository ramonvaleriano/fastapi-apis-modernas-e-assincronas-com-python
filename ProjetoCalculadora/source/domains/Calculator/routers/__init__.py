from fastapi import (
    APIRouter,
    Query,
    Header,
    Path
)
from typing import Optional

calculator_router = APIRouter()


@calculator_router.get('/calculator',
                       description='Soma simples de uma query string',
                       summary='Soma de dois números'
                       )
async def sum_calculator_duple(a: int, b: int):

    soma = a + b

    return soma


@calculator_router.get('/calculator2',
                       description='Soma de três numeros na query string',
                       summary='Soma de três números'
                       )
async def sum_calculator_triple(a: int, b: int, c: Optional[int] = 0):
    soma = a + b + c

    return soma


@calculator_router.get('/calculator3',
                       description='Soma de 4 número por query string',
                       summary='Soma de quatro números'
                       )
async def sum_calculator_fourth(a:  int = Query(default=None, ge=0), b: int = Query(default=None, ge=0), c: int = Query(default=None, ge=0), d: Optional[int] = 0):

    soma = a + b + c + d

    return soma


@calculator_router.get('/calculator4',
                       description='Soma de quatro número e uma mensagem bia Head',
                       summary='Soma de quartro números'
                       )
async def sum_calculator_fourth2(x_mensage: str = Header(default=None, title='Mensagem via Header'),
                                 a: int = Query(default=None, ge=0),
                                 b: int = Query(default=None, ge=0),
                                 c: int = Query(default=None, ge=0),
                                 d: Optional[int] = 0):

    soma = a + b + c + d
    return {
        'mensage': x_mensage,
        'sum': soma
    }


@calculator_router.get('/calculator5/{numero}', summary='O número elevado ao quadrado')
async def number_squared(numero: int):
    """
    Passaremos um número como Path Parameter e obteremos o quadrado dele\n
    :param numero: um número inteiro\n
    :return: número ao quadrado\n
    """
    result = numero ** 2

    return result


@calculator_router.get('/calculator6/{numero}',
                       summary='O quadrado do número passo via Path',
                       description='Passar um número via Path e ter o seu quadrado')
async def number_squared2(numero: int = Path(default=None,
                                             title='Número passado por Path',
                                             description='Qualquer número para retornar o seu quadrado'),
                          x_mensagem: str = Header(default=None, title='Mensagem passada via Header')
                          ):
    result = {
        'soma': numero ** 2,
        'mensagem': x_mensagem
    }

    return result
