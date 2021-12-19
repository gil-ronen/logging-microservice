from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class Log(Base):
    __tablename__ = "Log"
    id = Column(Integer, primary_key=True, index=True)
    asctime = Column(String(100)) #TODO Change to date
    name = Column(String(100))
    levelname = Column(String(100))
    message = Column(String(100))