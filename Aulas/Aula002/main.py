import uvicorn
from fastapi import FastAPI
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


@app.get('/cursos')
async def get_cursos():

    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({'id': curso_id})
    return curso

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
