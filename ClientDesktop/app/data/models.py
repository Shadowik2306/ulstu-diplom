from sqlalchemy import UniqueConstraint, CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


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
    music_url: Mapped[str]

    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id"))
    preset: Mapped["PresetModel"] = relationship(back_populates="samples")

    note_id: Mapped[int] = mapped_column(ForeignKey("Note.id"))

    __table_args__ = (
        UniqueConstraint('preset_id', 'note_id', name='uniq_notes_for_preset'),
        CheckConstraint('note_id IS NOT NULL AND note_id > 0', name='note_id_not_null'),
    )


class NoteModel(CustomBaseModel):
    __tablename__ = "Note"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

