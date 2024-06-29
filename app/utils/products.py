from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.models import Product, Task
from fastapi import HTTPException
from schemas.products import ProductCorp
from datetime import datetime



async def create_product(product_info:ProductCorp, session:AsyncSession):
    """ 
    Создание продукта в базе данных 

    Проверяется - существует указанный идентификатор продукта в бд, если нет -> error 400
    Существует ли указанная смена в бд, если нет -> error 404
    """
    product = await session.execute(select(Product).where(Product.product_id == product_info.product_id))
    product = product.scalars().first()
    if product:
        raise HTTPException(400, detail=f"Product_id '{product_info.product_id}' already exists ")
    task = await session.execute(select(Task).where(and_(Task.lot_number == product_info.lot_number,
                                                          Task.lot_date == product_info.lot_date )))
    task = task.scalars().first()
    if not task:
        raise HTTPException(404, f"Смена с данными 'Номер партии:{product_info.lot_number}'\
                             и 'ДатаПартии:{product_info.lot_date}' не найдены в БД")
    
    new_product = Product(product_id = product_info.product_id, task_id = task.id)
    session.add(new_product)
    await session.commit()
    return new_product

async def aggregate_product_and_task(task_id:int, product_id:str, session:AsyncSession):
    """
    Агрегация продукта и смены

    Проверяется - существует ли указанный продукт в бд, если нет -> error 404
    Связаны ли продукт и смена, если нет -> error 400 
    Агрегирован продукт, если да -> error 400 
    """

    product = await session.execute(select(Product).where(Product.product_id == product_id))
    product = product.scalars().first()

    if not product:
        raise HTTPException(404, 'Not found')
    if product.is_aggregated:
        raise HTTPException(400, f"unique code already used at {product.aggregated_at}")
    if not product.task_id == task_id:
        raise HTTPException(400, "unique code is attached to another batch")
    product.is_aggregated = True
    product.aggregated_at = datetime.now()
    await session.commit()
    return product
