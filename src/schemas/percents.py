from pydantic import BaseModel, Field

class SGetPercents(BaseModel):
    audience1:str = Field(description="SQL команда для локализации первой аудитории")
    audience2:str = Field(description="SQL команда для локализации первой аудитории")


class SPercents(BaseModel):
    percent:float = Field(default=None, description="Результат по запросу")
