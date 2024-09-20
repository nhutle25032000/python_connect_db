from typing import Optional
from typing import List
from sqlalchemy import Integer, TIMESTAMP, func, JSON, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.models.Base import Base

class Lora(Base):
    __tablename__ = "ai_job_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    checkpoint: Mapped[str] = mapped_column(String)
    images: Mapped[JSON] = mapped_column(JSON)
    status: Mapped[int] = mapped_column(Integer)
    gender: Mapped[int] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(string)
    trigger_word: Mapped[str] = mapped_column(string)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, onupdate=func.now())
    
    ai_job_data: Mapped[List["AiJobData"]] = relationship(back_populates="lora")
