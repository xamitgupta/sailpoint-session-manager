"""Data models for SailPoint Session Manager."""

from typing import Any, Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


class AppType(str, Enum):
    """Supported application types."""
    GOOGLE_WORKSPACE = "google_workspace"
    OKTA = "okta"
    AWS = "aws"
    SLACK = "slack"
    GENERIC = "generic"


class SessionStatus(str, Enum):
    """Session status."""
    ACTIVE = "active"
    IDLE = "idle"
    TERMINATED = "terminated"
    EXPIRED = "expired"


class TerminationStatus(str, Enum):
    """Session termination status."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Session:
    """Represents a user session in an application."""
    session_id: str
    user_id: str
    username: str
    app_type: AppType
    app_name: str
    status: SessionStatus
    created_at: datetime
    last_activity: Optional[datetime]
    device_info: Optional[str] = None
    ip_address: Optional[str] = None
    location: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def duration_minutes(self) -> int:
        """Calculate session duration in minutes."""
        delta = datetime.now() - self.created_at
        return int(delta.total_seconds() / 60)
    
    @property
    def idle_minutes(self) -> Optional[int]:
        """Calculate idle time in minutes."""
        if not self.last_activity:
            return None
        delta = datetime.now() - self.last_activity
        return int(delta.total_seconds() / 60)


@dataclass
class UserSessions:
    """All sessions for a user across all applications."""
    user_id: str
    username: str
    sailpoint_identity_id: str
    total_sessions: int
    active_sessions: List[Session]
    idle_sessions: List[Session]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TerminationRequest:
    """Request to terminate sessions."""
    request_id: str
    user_id: str
    username: str
    requested_by: str
    reason: str
    sessions_to_terminate: List[Session]
    status: TerminationStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    approval_status: Optional[str] = None
    approval_by: Optional[str] = None
    results: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SailPointConfig:
    """Configuration for SailPoint integration."""
    base_url: str
    api_username: str
    api_token: str
    verify_ssl: bool = True
    timeout: int = 30
