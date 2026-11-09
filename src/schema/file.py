from datetime import datetime 
from pathlib import Path
from pydantic import BaseModel, Field


class FileMetaData(BaseModel):

    name:str
    path: str
    extension: str

    size: int = Field(ge=0)

    created_at: datetime | None = None
    modified_at: datetime

    checksum: str | None = None

    is_readable: bool
    is_writable: bool

    file_type: str | None = None

    