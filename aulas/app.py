from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():

    return {'mensage': 'Tudo certo!'}
