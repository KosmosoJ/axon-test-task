from fastapi import APIRouter, Depends
from schemas.products import ProductCorp
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_session
from utils import products as products_utils


router = APIRouter()


@router.post('/product')
async def create_product(product_info:ProductCorp, session:AsyncSession=Depends(get_session)):
    product = await products_utils.create_product(product_info, session)
    return product

@router.put('/product')
async def aggreagate_product(product_id:str, task_id:int, session:AsyncSession = Depends(get_session)):
    product = await products_utils.aggregate_product_and_task(task_id=task_id, product_id=product_id, session=session)
    return product
