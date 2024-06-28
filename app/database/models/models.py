from sqlalchemy import Integer, String, Boolean, DateTime, Column, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from datetime import datetime




class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    close_status = Column(Boolean, default=False, comment='Статус закрытия')
    closed_at = Column(DateTime, default=None, comment='Время закрытия')
    task = Column(String, comment='Представление задания на смену')
    work_center = Column(String, comment='Рабочий центр')
    shift = Column(String, comment='Смена')
    crew = Column(String, comment='Бригада')
    lot_number = Column(Integer, comment='Номер партии')
    lot_date = Column(Date, default=datetime.now().date(), comment='Дата партии')
    name = Column(String, comment='Номенклатура')
    codeEKN = Column(String, comment='кодЕКН')
    DC_id = Column(String, comment='идентификатор РЦ ')
    shift_start = Column(DateTime, default=datetime.now())
    shift_end = Column(DateTime, default=None)

    parent = relationship('Product', back_populates='children')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    lot_number = (ForeignKey('tasks.lot_number'))
    lot_date = (ForeignKey('tasks.lot_date'))

    children = relationship('Task', back_populates='parent', lazy='joined', join_depth=4)