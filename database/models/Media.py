from typing import Optional
from sqlalchemy import Integer, TIMESTAMP, func, JSON, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.models.Base import Base

class Media(Base):
    __tablename__ = "ai_job_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_data_id: Mapped[int] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(string)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, onupdate=func.now())
