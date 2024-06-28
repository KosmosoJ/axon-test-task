from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tasks import TaskModel
from database.models.models import Task
from datetime import datetime




async def create_task(task_info:TaskModel, session:AsyncSession):
    check_lot = await session.execute(select(Task).where(Task.lot_number == task_info.lot_number))
    check_lot = check_lot.scalars().first()
    if check_lot:
        return None
    
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


