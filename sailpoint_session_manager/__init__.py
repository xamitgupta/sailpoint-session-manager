"""
SailPoint Session Manager - Multi-app session management and revocation tool.
"""

__version__ = "0.1.0"
__author__ = "Amit Gupta"
__email__ = "apphelp.csw@gmail.com"
__license__ = "MIT"

from sailpoint_session_manager.models import (
    Session,
    UserSessions,
    AppType,
    SessionStatus,
    TerminationRequest,
    TerminationStatus,
)
from sailpoint_session_manager.sailpoint_client import SailPointClient
from sailpoint_session_manager.connectors import ConnectorRegistry

__all__ = [
    "Session",
    "UserSessions",
    "AppType",
    "SessionStatus",
    "TerminationRequest",
    "TerminationStatus",
    "SailPointClient",
    "ConnectorRegistry",
]
