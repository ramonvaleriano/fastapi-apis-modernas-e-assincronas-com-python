from fastapi import APIRouter

calculator_router = APIRouter()


@calculator_router.get('/calculator')
async def sum_calculator():

    return {'mensage': 'Teste OK!'}