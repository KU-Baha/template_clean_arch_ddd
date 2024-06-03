from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/login')
async def login():
    pass


@auth_router.post('/logout')
async def logout():
    pass
