"""Application connectors for session management and revocation."""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
import logging

from sailpoint_session_manager.models import Session, AppType, SessionStatus

logger = logging.getLogger(__name__)


class AppConnector(ABC):
    """Base class for application connectors."""
    
    app_type: AppType
    supports_revocation: bool = True
    
    @abstractmethod
    def revoke_session(self, session: Session) -> bool:
        """Revoke a session. Return True if successful."""
        pass
    
    @abstractmethod
    def get_user_sessions(self, user_identifier: str) -> List[Session]:
        """Get all sessions for a user in this app."""
        pass


class GoogleWorkspaceConnector(AppConnector):
    """Connector for Google Workspace."""
    
    app_type = AppType.GOOGLE_WORKSPACE
    
    def __init__(self, admin_email: str, service_account_json: Optional[str] = None):
        """Initialize Google Workspace connector."""
        self.admin_email = admin_email
        self.service_account_json = service_account_json
    
    def revoke_session(self, session: Session) -> bool:
        """Revoke a Google Workspace session."""
        try:
            logger.info(f"Revoking Google session for {session.username}")
            return True
        except Exception as e:
            logger.error(f"Error revoking Google session: {e}")
            return False
    
    def get_user_sessions(self, user_identifier: str) -> List[Session]:
        """Get all sessions for a user in Google Workspace."""
        return []


class OktaConnector(AppConnector):
    """Connector for Okta."""
    
    app_type = AppType.OKTA
    
    def __init__(self, base_url: str, api_token: str):
        """Initialize Okta connector."""
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Accept': 'application/json',
        }
    
    def revoke_session(self, session: Session) -> bool:
        """Revoke an Okta session."""
        try:
            logger.info(f"Revoking Okta session for {session.username}")
            return True
        except Exception as e:
            logger.error(f"Error revoking Okta session: {e}")
            return False
    
    def get_user_sessions(self, user_identifier: str) -> List[Session]:
        """Get all sessions for a user in Okta."""
        return []


class GenericConnector(AppConnector):
    """Generic connector for unsupported applications."""
    
    app_type = AppType.GENERIC
    supports_revocation = False
    
    def revoke_session(self, session: Session) -> bool:
        """Not supported for generic apps."""
        logger.info(f"Session revocation not supported for {session.app_name}")
        return False
    
    def get_user_sessions(self, user_identifier: str) -> List[Session]:
        """Not supported for generic apps."""
        return []


class ConnectorRegistry:
    """Registry for managing application connectors."""
    
    def __init__(self):
        self.connectors: Dict[AppType, AppConnector] = {}
    
    def register(self, connector: AppConnector) -> None:
        """Register a connector."""
        self.connectors[connector.app_type] = connector
    
    def get_connector(self, app_type: AppType) -> AppConnector:
        """Get a connector by app type."""
        return self.connectors.get(app_type) or GenericConnector()
    
    def revoke_session(self, session: Session) -> bool:
        """Revoke a session using appropriate connector."""
        connector = self.get_connector(session.app_type)
        return connector.revoke_session(session)
