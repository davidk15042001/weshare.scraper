from pydantic import BaseModel, Field, validator
from typing import Optional

class ScrapeInputValidator(BaseModel):
    first_name:str
    last_name:str
    email:Optional[str] = Field(default="")
    phone:Optional[str] = Field(default="")
    country:Optional[str] = Field(default="")
    