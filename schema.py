from datetime import date
from pydantic import BaseModel

class Log(BaseModel):
    id = int
    asctime = str
    name = str
    levelname = str
    message = str

    class Config:
        orm_mode = True
