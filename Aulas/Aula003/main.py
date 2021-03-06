import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def status():

    return {
        'mensage': 'OK'
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, debug=True, reload=True)