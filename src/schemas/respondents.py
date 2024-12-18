from pydantic import BaseModel, Field

class SRespondents(BaseModel):
    id:int = Field("Уникальный идентификатор записи")
    Date:str = Field("Дата записи")
    respondent:int = Field("Уникальный номер респондента")
    Sex:int = Field("Пол 1 = М, 2 = Ж")
    Age:int = Field("Возраст респондента")
    Weight:float = Field("Некая стастистика респондента для этого времени записи")

