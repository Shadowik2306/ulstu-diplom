from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


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
    name: Mapped[str]
    music_url: Mapped[str]

    preset_id: Mapped[int] = mapped_column(ForeignKey("Preset.id"))
    preset: Mapped["PresetModel"] = relationship(back_populates="samples")