from typing import Optional
from sqlalchemy import Integer, TIMESTAMP, func, JSON, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.models.Base import Base

class ReferenceUrl(Base):
    __tablename__ = "ai_job_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(string)
    resize_url: Mapped[str] = mapped_column(string)
    crop_face_url: Mapped[str] = mapped_column(string)
    mask_url: Mapped[str] = mapped_column(string)
    transparent_url: Mapped[str] = mapped_column(string)
    coordinate_x: Mapped[int] = mapped_column(Integer)
    coordinate_y: Mapped[int] = mapped_column(Integer)
    page_index: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, onupdate=func.now())
