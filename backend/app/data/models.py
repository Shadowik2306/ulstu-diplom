from sqlalchemy import ForeignKey, UniqueConstraint, event
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship, Session


class CustomBaseModel(DeclarativeBase):
    pass


class PresetModel(CustomBaseModel):
    __tablename__ = "Preset"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete="CASCADE"))
    user: Mapped["UserModel"] = relationship(back_populates="presets")

    name: Mapped[str]
    color: Mapped[str]

    samples: Mapped[list['SampleModel']] = relationship(back_populates='preset', lazy='selectin')


class SampleModel(CustomBaseModel):
    __tablename__ = "Sample"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id", ondelete="CASCADE"))
    preset: Mapped["PresetModel"] = relationship(back_populates="samples")

    music_id: Mapped[int] = mapped_column(ForeignKey("Music.id", ondelete="CASCADE"))
    music: Mapped["MusicModel"] = relationship(back_populates="used_by", lazy='selectin')

    note_id: Mapped[int] = mapped_column(ForeignKey("Notes.id"), nullable=True)

    @property
    def music_url(self):
        return self.music.music_url

    __table_args__ = (
        UniqueConstraint('preset_id', 'note_id', name='uniq_notes_for_preset'),
    )


class MusicModel(CustomBaseModel):
    __tablename__ = 'Music'

    id: Mapped[int] = mapped_column(primary_key=True)
    music_url: Mapped[str]

    used_by: Mapped[list['SampleModel']] = relationship(back_populates='music', lazy='selectin')



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
    favorites: Mapped[list["PresetModel"]] = relationship(secondary='UserFavorites', lazy='selectin')


class UserFavorites(CustomBaseModel):
    __tablename__ = 'UserFavorites'

    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), primary_key=True)
    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id"), primary_key=True)


class JwtBlackListModel(CustomBaseModel):
    __tablename__ = 'jwt_black_list'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str]

