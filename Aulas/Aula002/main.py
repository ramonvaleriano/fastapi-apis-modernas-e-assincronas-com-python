import uvicorn
from fastapi import (
    FastAPI,
    HTTPException,
    status
)
from models import CursosModel

app = FastAPI()

cursos = {
    1: {
        'titulo': 'Programação para Leigos',
        'aulas': 112,
        'horas': 58
    },
    2: {
        'titulo': 'Algoritmo e lógica de programação',
        'aulas': 87,
        'horas': 67
    }
}


@app.get('/cursos', status_code=status.HTTP_200_OK, tags=['Coletando todos os cursos'])
async def get_cursos():

    return cursos


@app.get('/cursos/{curso_id}', status_code=status.HTTP_200_OK, tags=['Coletando um Curso especifico'])
async def get_curso(curso_id: int):
    print(curso_id)
    try:
        curso = cursos[curso_id]
        curso.update({'id': curso_id})
        return curso

    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED, tags=['Adicionando um Curso no banco de dados'])
async def add_curso(curso: CursosModel):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso

    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Já existe esse ID no banco')

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
