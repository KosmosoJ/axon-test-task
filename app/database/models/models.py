from sqlalchemy import Integer, String, Boolean, DateTime, Column, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database.database import Base
from datetime import datetime




class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    close_status = Column(Boolean, default=False, comment='Статус закрытия')
    closed_at = Column(TIMESTAMP(timezone=True), server_default=None, comment='Время закрытия')
    task = Column(String, comment='Представление задания на смену')
    work_center = Column(String, comment='Рабочий центр')
    shift = Column(String, comment='Смена')
    crew = Column(String, comment='Бригада')
    lot_number = Column(Integer, comment='Номер партии')
    lot_date = Column(Date, comment='Дата партии')
    name = Column(String, comment='Номенклатура')
    codeEKN = Column(String, comment='кодЕКН')
    DC_id = Column(String, comment='идентификатор РЦ ')
    shift_start = Column(TIMESTAMP(timezone=True))
    shift_end = Column(TIMESTAMP(timezone=True), server_default=None)



class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    product_id = Column(String)
    task_id = Column(Integer, ForeignKey('tasks.id'), default=None)
    # lot_number_r = relationship('Task', foreign_keys=[lot_number])
    
    is_aggregated = Column(Boolean, default=False)
    aggregated_at = Column(TIMESTAMP(timezone=True))
    # lot_date_r = relationship('Task', foreign_keys=[lot_date])

    # task = relationship('Task', back_populates='products', primaryjoin='Product.lot_number == Task.lot_number')