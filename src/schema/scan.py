from datetime import datetime
from pydantic import BaseModel, Field

class ScanResult(BaseModel):

    scan_id: str

    directory: str

    started_at: datetime

    completed_at: datetime | None = None

    total_files: int = Field(default=0, ge=0)

    valid_files: int = Field(default=0, ge=0)

    invalid_files: int = Field(default=0, ge=0)

    errors: list[str] = Field(default_factory=list)