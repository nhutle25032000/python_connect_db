from typing import Optional
from sqlalchemy import Integer, TIMESTAMP, func, JSON, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.models.Base import Base

class AiJobData(Base):
    __tablename__ = "ai_job_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    lora_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[str] = mapped_column(String)
    status: Mapped[int] = mapped_column(Integer)
    ai_generate_type: Mapped[int] = mapped_column(Integer)
    ai_generate_data: Mapped[JSON] = mapped_column(JSON)
    processing_results: Mapped[Optional[JSON]] = mapped_column(JSON)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, onupdate=func.now())
    reference_url_id: Mapped[Optional[int]] = mapped_column(Integer)
    
    lora: Mapped["Lora"] = relationship(back_populates="ai_job_data")
    
    def __repr__(self):
        return (f"AiJobData(id={self.id}, lora_id={self.lora_id}, user_id={self.user_id}, "
                f"status={self.status}, ai_generate_type={self.ai_generate_type}, "
                f"ai_generate_data={self.ai_generate_data}, "
                f"processing_results={self.processing_results}, "
                f"created_at={self.created_at}, updated_at={self.updated_at}, "
                f"reference_url_id={self.reference_url_id})")