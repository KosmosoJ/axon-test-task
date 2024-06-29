from pydantic import BaseModel, Field
from datetime import date 

class ProductModel(BaseModel):
    product_id:str

class ProductCorp(BaseModel):
    product_id:str = Field(alias='УникальныйКодПродукта', validation_alias='УникальныйКодПродукта')
    lot_number:int = Field(alias='НомерПартии', validation_alias='НомерПартии')
    lot_date:date = Field(alias='ДатаПартии', validation_alias='ДатаПартии')