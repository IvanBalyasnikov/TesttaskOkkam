from src.repositories.respondents import RespondentsRepository
from src.database import async_session_maker
from src.services.base import BaseService
from src.schemas.percents import SGetPercents, SPercents
from src.schemas.respondents import SRespondents

import pandas as pd

class PercentsService(BaseService):
    session_maker = async_session_maker
    schema:SPercents
    repository = RespondentsRepository

    async def get(self, data:SGetPercents) -> SPercents:
        async with async_session_maker() as session:
            respondents1:list[SRespondents] = await self.repository(session).query_audience(data.audience1)
            respondents2:list[SRespondents] = await self.repository(session).query_audience(data.audience2)
        if len(respondents1) == 0 or len(respondents2) == 0:
            return SPercents(percent=None)
        

        respondents1_df = pd.DataFrame([s.__dict__ for s in respondents1])
        respondents2_df = pd.DataFrame([s.__dict__ for s in respondents2])

        avg_weight_per_respondent1 = respondents1_df.groupby('respondent', as_index=False)['Weight'].mean()
        avg_weight_per_respondent2 = respondents2_df.groupby('respondent', as_index=False)['Weight'].mean()

        resp_set_1 = set(avg_weight_per_respondent1['respondent'])
        resp_set_2 = set(avg_weight_per_respondent2['respondent'])

        intersection = resp_set_1.intersection(resp_set_2)

        sum_avg_1 = avg_weight_per_respondent1['Weight'].sum()
        intersection_df_1 = avg_weight_per_respondent1[avg_weight_per_respondent1['respondent'].isin(intersection)]

        sum_intersection = intersection_df_1['Weight'].sum()

        percent = sum_intersection / sum_avg_1 if sum_avg_1 != 0 else 0

        return SPercents(percent=percent)


        

        

        

        
        




