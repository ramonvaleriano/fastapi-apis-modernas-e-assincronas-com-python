import uvicorn
from fastapi import (
    FastAPI,
    Query,
    Header
)
from typing import Optional
from routers.curso_router import curso_router

app = FastAPI(
    title='Api de Cursos',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
)

app.include_router(curso_router, prefix='/api/v1')


@app.get('/calculadora', tags=['Programando a Calculadora'])
async def calcular(a: int, b: int, c: Optional[int] = 0):

    soma = a + b + c

    return {'mensagem': soma}


@app.get('/calculadora2', tags=['Programando a Calculadora'])
async def calcular2(a: int = Query(default=None, ge=0), b: int = Query(default=None, ge=0), c: Optional[int] = 0):

    soma = a + b + c

    return {'mensagem': soma}


@app.get('/calculadora3', tags=['Programando a Calculadora'])
async def calculadora3(a: int = Query(default=None, ge=0), b: int = Query(default=None, ge=0),
                       x_geek: str = Header(default=None), c: Optional[int] = 0):

    soma = a + b + c
    print(f'Testando header: {x_geek}')

    return {'SomaDoBugulhoDoido': soma}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
