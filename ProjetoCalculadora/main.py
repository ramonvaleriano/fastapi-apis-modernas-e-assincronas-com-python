import uvicorn
from fastapi import FastAPI
from source.routers import router_projeto

app = FastAPI()
app.include_router(router_projeto)


@app.get('/')
async def status():

    return {'mensage': 'OK!'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)

