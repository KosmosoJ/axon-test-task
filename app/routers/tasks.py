from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import tasks
from utils import tasks as task_utils

router = APIRouter()

@router.get('/task/{id}', response_model=tasks.TaskModel)
async def get_task(id:int, session:AsyncSession = Depends(get_session)):

    ...

@router.post('/task/', response_model=tasks.TaskModel)
async def post_task(task_info:tasks.TaskModel, session:AsyncSession = Depends(get_session)):
    # print(task_info.shift_start)?
    task = await task_utils.create_task(task_info=task_info,session= session)
    return task_info