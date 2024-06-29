from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy import select, or_
from database.models.models import Task
from datetime import date, datetime
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import tasks
from utils import tasks as task_utils

router = APIRouter()

@router.get('/task/{id}', response_model=tasks.TaskModel)
async def get_task(id:int, session:AsyncSession = Depends(get_session)):
    task = await task_utils.get_task(id, session)
    if not task:
        raise HTTPException(status_code=404, detail=f"Задание с id '{id}' не найдено")
    return tasks.TaskModel(СтатусЗакрытия=task.close_status,
                            ПредставлениеНаСмену=task.task,
                            Линия='?',
                            Смена=task.shift,
                            Бригада=task.crew,
                            НомерПартии=task.lot_number,
                            ДатаПартии=task.lot_date,
                            Номенклатура=task.name,
                            КодЕКН=task.codeEKN,
                            ИдентификаторРЦ=task.DC_id,
                            ДатаВремяНачалаСмены=task.shift_start,
                            ДатаВремяОкончанияСмены=task.shift_end)

@router.get('/task')
async def get_task_filter(crew:str=Query(None),
                          shift:str=Query(None),
                          lot_number:int=Query(None),
                          lot_date:str=Query(None),
                          codeEKN:str = Query(None),
                          close_status:bool = Query(None),
                          offset:int = 1,
                          limit:int = 10,
                          session:AsyncSession = Depends(get_session)):
    
    task = await task_utils.get_filter_task(crew, shift, lot_number, lot_date, codeEKN, close_status,offset,limit, session)
    return task

@router.post('/task/', response_model=tasks.TaskModel)
async def post_task(task_info:tasks.TaskModel, session:AsyncSession = Depends(get_session)):
    task = await task_utils.create_task(task_info=task_info,session= session)
    return task_info

@router.put('/task/{task_id}')
async def put_task(task_id:int,task_info:tasks.TaskModel, session:AsyncSession = Depends(get_session)):
    task = await task_utils.edit_task(task_id=task_id, task_info=task_info, session=session)
    return task 