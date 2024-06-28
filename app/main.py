from fastapi import FastAPI

from routers import products, tasks


app = FastAPI()


app.include_router(products.router, prefix='/api',tags=['products'])
app.include_router(tasks.router,prefix='/api', tags=['tasks'])


@app.get('/')
async def main():
    return {'Message':'App started'}
    