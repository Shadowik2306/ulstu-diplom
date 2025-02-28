from sqlalchemy import select

from app.data.database import async_session_maker
from app.data.models import NoteModel

notes_data = [
    {"id": 1, "name": "C"},
    {"id": 2, "name": "C#"},
    {"id": 3, "name": "D"},
    {"id": 4, "name": "D#"},
    {"id": 5, "name": "E"},
    {"id": 6, "name": "F"},
    {"id": 7, "name": "G"},
    {"id": 8, "name": "D#"}
]


class NoteRepository:
    @classmethod
    async def initialize_table(cls):
        async with async_session_maker() as session:
            for note in notes_data:
                query = select(NoteModel).where(note["id"] == NoteModel.id)

                res = await session.execute(query)

                if res.one_or_none():
                    continue

                new_note = NoteModel(**note)
                session.add(new_note)
                await session.commit()
