from sqlalchemy import ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class CustomBaseModel(DeclarativeBase):
    pass


class PresetModel(CustomBaseModel):
    __tablename__ = "Preset"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user: Mapped["UserModel"] = relationship(back_populates="presets")

    name: Mapped[str]
    color: Mapped[str]

    samples: Mapped[list['SampleModel']] = relationship(back_populates='preset', lazy='selectin')


class SampleModel(CustomBaseModel):
    __tablename__ = "Sample"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    music_url: Mapped[str]

    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id"))
    preset: Mapped["PresetModel"] = relationship(back_populates="samples")

    note_id: Mapped[int] = mapped_column(ForeignKey("Notes.id"), nullable=True)

    __table_args__ = (
        UniqueConstraint('preset_id', 'note_id', name='uniq_notes_for_preset'),
    )


class NoteModel(CustomBaseModel):
    __tablename__ = "Notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class UserModel(CustomBaseModel):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]

    presets: Mapped[list["PresetModel"]] = relationship(back_populates="user", lazy='selectin')


class JwtBlackListModel(CustomBaseModel):
    __tablename__ = 'jwt_black_list'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str]

