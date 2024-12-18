from sqlalchemy import insert, select, text
from src.schemas.respondents import SRespondents
from src.models.respondents import RespondentsOrm
from src.repositories.base import BaseRepository


class RespondentsRepository(BaseRepository):
    model = RespondentsOrm
    schema = SRespondents

    async def query_audience(self, query:str) -> list[SRespondents]:
        
        query_audience = (
            select(RespondentsOrm)
            .filter(text(query.lower()))
            # .group_by(self.model.respondent)
        )
        result = await self.session.execute(query_audience)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]


    async def create(self, data:SRespondents) -> SRespondents:
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        model = result.scalars().one_or_none()
        return self.schema.model_validate(model, from_attributes=True)
    
    async def bulk_create(self, data:SRespondents) -> None:
        data = [self.model(**schema.dict()) for schema in data]
        async with self.session.begin():
            self.session.add_all(data)




   