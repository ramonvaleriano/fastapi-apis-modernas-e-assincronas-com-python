from fastapi import FastAPI

app = FastAPI()


@app.get('/msg')
async def mensagem():

    return {'mensage': 'Tudo certo!'}
