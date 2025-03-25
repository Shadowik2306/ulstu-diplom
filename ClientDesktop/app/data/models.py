import numpy as np
from sqlalchemy import UniqueConstraint, CheckConstraint, ForeignKey, TypeDecorator, LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import pickle


class CustomBaseModel(DeclarativeBase):
    pass


class PresetModel(CustomBaseModel):
    __tablename__ = "Preset"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    samples: Mapped[list['SampleModel']] = relationship(back_populates='preset', lazy='selectin')


class SampleModel(CustomBaseModel):
    __tablename__ = "Sample"

    id: Mapped[int] = mapped_column(primary_key=True)

    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id"))
    preset: Mapped["PresetModel"] = relationship(back_populates="samples")

    note_id: Mapped[int] = mapped_column(ForeignKey("Note.id"))

    data: Mapped[bytes] = mapped_column(LargeBinary)

    def set_data(self, list_of_arrays):
        self.data = pickle.dumps(list_of_arrays)

    def get_data(self):
        if self.data is not None:
            return pickle.loads(self.data)
        return None

    __table_args__ = (
        UniqueConstraint('preset_id', 'note_id', name='uniq_notes_for_preset'),
        CheckConstraint('note_id IS NOT NULL AND note_id > 0', name='note_id_not_null'),
    )


class NoteModel(CustomBaseModel):
    __tablename__ = "Note"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

