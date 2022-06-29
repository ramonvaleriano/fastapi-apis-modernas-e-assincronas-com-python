import uvicorn
from fastapi import FastAPI
from models import Aula002Model

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


@app.get('/')
async def home():

    return {'mensage': 'Tudo certo'}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
