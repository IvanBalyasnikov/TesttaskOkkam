from typing import Annotated
from fastapi import APIRouter, Depends
from src.schemas.percents import SGetPercents, SPercents
from src.services.percents import PercentsService



router = APIRouter(prefix="",
                   tags = ["Ручка для получения вхождения аудиторий"])




@router.get("/getPercent")
async def get_percent(
    data:Annotated[SGetPercents, Depends(SGetPercents)]
) -> SPercents:
    return await PercentsService().get(data)
    
    




