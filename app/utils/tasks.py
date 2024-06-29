from sqlalchemy import select,insert, update, and_, or_
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tasks import TaskModel
from database.models.models import Task
from datetime import datetime


async def insert_info_in_task(task:Task, task_info:TaskModel,time:bool = False):
    request = update(Task).where(Task.id == task.id).values(
        close_status = task_info.close,
        task = task_info.task,
        closed_at = datetime.now() if time else None,
        work_center = '1',
        shift = task_info.shift,
        crew = task_info.crew,
        lot_number = task_info.lot_number,
        lot_date = task_info.lot_date,
        name = task_info.name,
        codeEKN = task_info.codeEKN,
        DC_id = task_info.DC_id,
        shift_start = task_info.shift_start,
        shift_end = task_info.shift_end
    )
    return request

async def create_task(task_info:TaskModel, session:AsyncSession):
    check_lot = await session.execute(select(Task).where(and_(Task.lot_number == task_info.lot_number, Task.lot_date == task_info.lot_date)))
    check_lot = check_lot.scalars().first()
    if check_lot:
        task= await session.execute(await insert_info_in_task(check_lot, task_info))

        await session.commit()
        return task
    
    task = Task(
    close_status = task_info.close,
    task = task_info.task,
    work_center = '1',
    shift = task_info.shift,
    crew = task_info.crew,
    lot_number = task_info.lot_number,
    lot_date = task_info.lot_date,
    name = task_info.name,
    codeEKN = task_info.codeEKN,
    DC_id = task_info.DC_id,
    shift_start = task_info.shift_start,
    shift_end = task_info.shift_end
)
    session.add(task)
    await session.commit()
    return task 

async def get_task(task_id:int, session:AsyncSession):
    task = await session.execute(select(Task).where(Task.id == task_id))
    task = task.scalars().first()
    if not task:
        return None
    return task

async def get_filter_task(crew:str, shift:str, lot_number:int, lot_date:str, codeEKN:str, close_status:bool, offset,limit:int, session:AsyncSession):
    if lot_date:
        lot_date = datetime.strptime(lot_date.replace('.', '-').replace(',','-'), '%d-%m-%Y').date()
    result = await session.execute(select(Task).offset((offset -1)*limit).filter(or_(Task.crew == crew, Task.shift == shift,
                                                            Task.lot_number == lot_number,
                                                            Task.lot_date == lot_date,
                                                            Task.codeEKN == codeEKN,
                                                            Task.close_status == close_status)).limit(limit))
    result = result.scalars().all()
    if not result:
        raise HTTPException(status_code=404, detail='Not found')
    return result 

async def edit_task(task_id:int,task_info:TaskModel, session:AsyncSession):
    task = await session.execute(select(Task).where(Task.id == task_id))
    task = task.scalars().first()
    if not task:
        raise HTTPException(404, 'Not found')
    edited_task = await session.execute(await insert_info_in_task(task,task_info, True))
    await session.commit()
    return task

