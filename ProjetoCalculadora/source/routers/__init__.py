from fastapi import APIRouter
from source.domains.Calculator.routers import calculator_router

router_projeto = APIRouter()

# Rotas da calculadora
router_projeto.include_router(calculator_router, prefix='/api/v1', tags=['Formas de Caclular via GET'])
