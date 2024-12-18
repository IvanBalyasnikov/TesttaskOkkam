import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from repositories.respondents import RespondentsRepository
from schemas.respondents import SRespondents
from database import async_session_maker
import pandas as pd
import asyncio




async def main():
    async with async_session_maker() as session:
        test = await RespondentsRepository(session).query_audience("where id > 0 and id < 2")
        if test:
            return
    df = pd.read_csv("data 1.csv")
    lists = [j[0].split(";") for j in df.values.tolist()]
    data = [SRespondents(id = int(record[0]), Date=str(record[1]), respondent=int(record[2]), Sex=int(record[3]), Age=int(record[4]), Weight=float(record[5])) for record in lists]
    async with async_session_maker() as session:
        await RespondentsRepository(session).bulk_create(data)
        await session.commit()




if __name__ == "__main__":
    asyncio.run(main())