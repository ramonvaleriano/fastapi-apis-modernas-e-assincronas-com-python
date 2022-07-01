import uvicorn
from fastapi import FastAPI
from source.routers import router_projeto

app = FastAPI(title='Calculadora', version='0.0.1', description='Uma api para testar as Query String e Path')
app.include_router(router_projeto)


@app.get('/')
async def status():

    return {'mensage': 'OK!'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)
