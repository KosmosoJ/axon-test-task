from pydantic import BaseModel, Field, AliasPath, AliasChoices
from datetime import  date, datetime



class TaskModel(BaseModel):
    close:bool = Field(alias='СтатусЗакрытия', validation_alias='СтатусЗакрытия')
    task:str = Field(alias='ПредставлениеНаСмену', validation_alias='ПредставлениеНаСмену')
    line:str = Field(alias='Линия', validation_alias='Линия')
    shift:str = Field(alias='Смена', validation_alias='Смена')
    crew:str = Field(alias='Бригада', validation_alias='Бригада')
    lot_number:int = Field(alias='НомерПартии', validation_alias='НомерПартии')
    lot_date:date = Field(alias='ДатаПартии',validation_alias='ДатаПартии')
    name:str = Field(alias='Номенклатура', validation_alias='Номенклатура')
    codeEKN:str = Field(alias='КодЕКН', validation_alias='КодЕКН')
    DC_id:str = Field(alias='ИдентификаторРЦ', validation_alias='ИдентификаторРЦ')
    shift_start:datetime= Field(alias='ДатаВремяНачалаСмены', validation_alias='ДатаВремяНачалаСмены')
    shift_end:datetime = Field(alias='ДатаВремяОкончанияСмены', validation_alias='ДатаВремяОкончанияСмены')
    

