from pydantic import BaseModel
from typing import Optional


class Delete(BaseModel):
    message: Optional[str] = "Deleted successfully"
    id: str

    class Config:
        orm_mode = True
