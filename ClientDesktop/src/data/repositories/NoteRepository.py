from sqlalchemy import select

from src.data.database import session_maker
from src.data.models import NoteModel

notes_data = [
    {"id": 1, "name": "C"},
    {"id": 2, "name": "C#"},
    {"id": 3, "name": "D"},
    {"id": 4, "name": "D#"},
    {"id": 5, "name": "E"},
    {"id": 6, "name": "F"},
    {"id": 7, "name": "F#"},
    {"id": 8, "name": "G"},
    {"id": 9, "name": "G#"},
    {"id": 10, "name": "A"},
    {"id": 11, "name": "A#"},
    {"id": 12, "name": "B"}
]


class NoteRepository:
    @classmethod
    def initialize_table(cls):
        with session_maker() as session:
            for note in notes_data:
                query = select(NoteModel).where(note["id"] == NoteModel.id)

                res = session.execute(query)
                note_model = res.scalar()

                if note_model:
                    continue

                new_note = NoteModel(**note)
                session.add(new_note)
                session.commit()
