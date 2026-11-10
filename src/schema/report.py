from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class ReportStatus(str, Enum):
    COMPLETED = "completed"
    COMPLETED_WITH_ERRORS = "completed_with_errors"
    FAILED = "failed"


class ReportSummary(BaseModel):
    total_files: int = Field(default=0, ge=0)
    valid_files: int = Field(default=0, ge=0)
    invalid_files: int = Field(default=0, ge=0)
    unreadable_files: int = Field(default=0, ge=0)
    modified_files: int = Field(default=0, ge=0)
    deleted_files: int = Field(default=0, ge=0)
    new_files: int = Field(default=0, ge=0)
    duplicate_files: int = Field(default=0, ge=0)
    total_size_bytes: int = Field(default=0, ge=0)


class ReportIssue(BaseModel):
    file_path: str | None = None
    category: str
    severity: str
    message: str
    detected_at: datetime = Field(
        default_factory=datetime.now
    )


class ScanReport(BaseModel):
    report_id: str
    scan_id: str

    status: ReportStatus

    directory: str

    started_at: datetime
    completed_at: datetime | None = None

    summary: ReportSummary = Field(
        default_factory=ReportSummary
    )

    issues: list[ReportIssue] = Field(
        default_factory=list
    )

    generated_at: datetime = Field(
        default_factory=datetime.now
    )