from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products, tasks


app = FastAPI()


app.include_router(products.router, prefix='/api',tags=['products'])
app.include_router(tasks.router,prefix='/api', tags=['tasks'])


origins = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:8005',
    'http://localhost',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.get('/')
async def main():
    return {'Message':'App started'}
    