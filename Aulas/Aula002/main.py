import uvicorn
from time import sleep
from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Response,
    Path,
    Query,
    Header,
    Depends
)
from models import CursosModel
from typing import Optional, Any, List, Dict


def fake_db():
    try:
        print('Abrindo Conexão com o banco de dados')
        sleep(1)
    finally:
        print('Fechando Conexão com o banco de dados')
        sleep(1)


app = FastAPI(
    title='Api de Cursos',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
)

cursos = [
    CursosModel(id=1, titulo='Programação para leigos', aulas=42, horas=56),
    CursosModel(id=2, titulo='Python para todos', aulas=49, horas=45)
]


@app.get('/cursos', status_code=status.HTTP_200_OK, tags=['Coletando todos os cursos'],
         description='Rota responsável pela coleta de todos os cursos, ou um lista vazia',
         summary='Rota com lista de Cursos ou lista Vazia',
         response_model=list[CursosModel],
         response_description='Cursos encontrados com sucesso')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}', status_code=status.HTTP_200_OK, tags=['Coletando um Curso especifico'],
         description='Rota para coletar curso único',
         summary='Coletar curso por id',
         response_model=CursosModel)
async def get_curso(curso_id: int = Path(default=None, title='ID do Curso', description='Deve ser entre 1 e 2',
                                         gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        for curso in cursos:
            if curso_id == curso.id:
                return curso
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED, tags=['Adicionando um Curso no banco de dados'],
          description='Rota responsável por adicionar um novo curso.',
          summary='Adiconar um curso novo',
          response_model=CursosModel)
async def add_curso(curso: CursosModel, db: Any = Depends(fake_db)):
    try:
        next_id = len(cursos) + 1
        curso_para_add = CursosModel(id=next_id, titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
        cursos.append(curso_para_add)

        return curso_para_add

    except Exception as error:

        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Problema ao Inserir dados no banco: {error}')


@app.put('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED, tags=['Atualizando curso de forma individual'],
         description='Rota responsável por atulizar determinado curso',
         summary='Atualizar curso',
         response_model=CursosModel)
async def update_curso(curso: CursosModel, curso_id: int = Path(default=None, title='ID do curso',
                       description='Adicione o Id que deseja atualizar'),
                       db: Any = Depends(fake_db)):
    id_ = False
    curso_para_atualizar = None

    for index_, curso_ in enumerate(cursos):
        if curso_id == curso_.id:
            curso_para_atualizar = CursosModel(id=curso_id, titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
            id_ = index_
            break

    if type(id_) == int:
        cursos[id_] = curso_para_atualizar
        return curso_para_atualizar

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não exite esse curso para ser atualizado')


@app.delete('/cursos/{curso_id}', status_code=status.HTTP_205_RESET_CONTENT, tags=['Deletando curso de forma individual'],
            summary='Deletar um curso')
async def delete_curso(curso_id: int = Path(default=None, title='ID do curso que deseja deletar',
                       description='Uso o ID para deletar o curso'),
                       db: Any = Depends(fake_db)):
    """
    Usar essa rota apenas no caso de querer deletar um curso\n
    :param curso_id: ID do curso\n
    :return: status 204 para o caso de ter sido com sucesso e 404 de ter falho
    """
    id_ = False

    for index_, curso in enumerate(cursos):
        if curso.id == curso_id:
            id_ = index_

    if type(id_) == int:
        del cursos[id_]
        #return responses.JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content='Curso apagado com sucesso')
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não foi encontrado arquivo para se deletar')


@app.get('/calculadora', tags=['Programando a Calculadora'])
async def calcular(a: int, b: int, c: Optional[int] = 0, db: Any = Depends(fake_db)):

    soma = a + b + c

    return {'mensagem': soma}


@app.get('/calculadora2', tags=['Programando a Calculadora'])
async def calcular2(a: int = Query(default=None, ge=0), b: int = Query(default=None, ge=0), c: Optional[int] = 0,
                    db: Any = Depends(fake_db)):

    soma = a + b + c

    return {'mensagem': soma}


@app.get('/calculadora3', tags=['Programando a Calculadora'])
async def calculadora3(a: int = Query(default=None, ge=0), b: int = Query(default=None, ge=0),
                       x_geek: str = Header(default=None), c: Optional[int] = 0, db: Any = Depends(fake_db)):

    soma = a + b + c
    print(f'Testando header: {x_geek}')

    return {'SomaDoBugulhoDoido': soma}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
