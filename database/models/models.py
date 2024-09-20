from typing import Optional
from sqlalchemy import Integer, TIMESTAMP, func, JSON, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

class Base(DeclarativeBase):
    pass

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
    
    def __repr__(self):
        return (f"AiJobData(id={self.id}, lora_id={self.lora_id}, user_id={self.user_id}, "
                f"status={self.status}, ai_generate_type={self.ai_generate_type}, "
                f"ai_generate_data={self.ai_generate_data}, "
                f"processing_results={self.processing_results}, "
                f"created_at={self.created_at}, updated_at={self.updated_at}, "
                f"reference_url_id={self.reference_url_id})")

# Thông tin kết nối
#user = 'headha_admin_prod'
#password = 'DAod+N<uj4Ry+rQtzrvLeT2&*2PnQ'
#host = 'snafty-headswap-prod.cn5cjf5ay4r8.us-east-1.rds.amazonaws.com'
#port = 3306
#database = 'snafty_headswap_prod'
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'headswap'

# Tạo engine kết nối
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

#with Session(engine) as session:
#    spongebob = AiJobData(
#        lora_id=112,
#        user_id="Spongebob Squarepants",
#        status=2,
#        ai_generate_type=2,
#        ai_generate_data={"result": "success"}
#    )
#
#    session.add_all([spongebob])
#
#    session.commit()
    
session = Session(engine)
stmt = select(AiJobData).where(AiJobData.id == 1)
#users = session.scalars(stmt)
for user in session.scalars(stmt):
    print(user)
#print(users)
#patrick = session.scalars(stmt).one()
#patrick.status = 3
#patrick.updated_at = func.now()

#session.commit()