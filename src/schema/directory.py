from datetime import datetime 
from pathlib import Path
from pydantic import BaseModel, Field


class DirectoryMetaData(BaseModel):

    name:str
    path: str
    owner_permission: str
    
    size: int = Field(ge=0)
    number_of_sub_directories: int = Field(ge=0)

    created_at: datetime | None = None
    modified_at: datetime

    checksum: str | None = None

   

    