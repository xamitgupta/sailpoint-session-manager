"""SailPoint API client for identity and account management."""

import requests
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

from sailpoint_session_manager.models import SailPointConfig, UserSessions, Session, AppType, SessionStatus

logger = logging.getLogger(__name__)


class SailPointClient:
    """Client for interacting with SailPoint API."""
    
    def __init__(self, config: SailPointConfig):
        """Initialize SailPoint client."""
        self.config = config
        self.base_url = config.base_url.rstrip('/')
        self.session = requests.Session()
        self.session.auth = (config.api_username, config.api_token)
        self.session.verify = config.verify_ssl
        self.session.timeout = config.timeout
        self.session.headers.update({'Accept': 'application/json'})
    
    def get_applications(self) -> List[Dict[str, Any]]:
        """Get list of connected applications from SailPoint."""
        try:
            url = f"{self.base_url}/api/identityiq/application"
            response = self.session.get(url)
            response.raise_for_status()
            apps = response.json()
            if isinstance(apps, dict) and 'resources' in apps:
                return apps['resources']
            return apps if isinstance(apps, list) else []
        except Exception as e:
            logger.error(f"Failed to get applications: {e}")
            return []
    
    def get_identity(self, username: str) -> Optional[Dict[str, Any]]:
        """Get identity by username."""
        try:
            url = f"{self.base_url}/api/identityiq/user"
            params = {'filter': f'name eq "{username}"'}
            response = self.session.get(url, params=params)
            response.raise_for_status()
            result = response.json()
            if isinstance(result, dict) and 'resources' in result:
                resources = result['resources']
                return resources[0] if resources else None
            elif isinstance(result, list):
                return result[0] if result else None
            return result
        except Exception as e:
            logger.error(f"Failed to get identity {username}: {e}")
            return None
    
    def get_accounts_for_identity(self, identity_id: str) -> List[Dict[str, Any]]:
        """Get all accounts linked to an identity."""
        try:
            url = f"{self.base_url}/api/identityiq/account"
            params = {'filter': f'identityId eq "{identity_id}"'}
            response = self.session.get(url, params=params)
            response.raise_for_status()
            result = response.json()
            if isinstance(result, dict) and 'resources' in result:
                return result['resources']
            return result if isinstance(result, list) else []
        except Exception as e:
            logger.error(f"Failed to get accounts: {e}")
            return []
    
    def get_user_sessions(self, username: str) -> Optional[UserSessions]:
        """Get all sessions for a user across all applications."""
        try:
            identity = self.get_identity(username)
            if not identity:
                return None
            
            identity_id = identity.get('id') or identity.get('name')
            accounts = self.get_accounts_for_identity(identity_id)
            
            sessions = []
            for account in accounts:
                app_name = account.get('applicationName', 'Unknown')
                app_type = self._detect_app_type(app_name)
                created_at = self._parse_date(account.get('created'))
                last_activity = self._parse_date(account.get('lastUpdated'))
                
                status = SessionStatus.ACTIVE
                if last_activity:
                    idle_minutes = (datetime.now() - last_activity).total_seconds() / 60
                    if idle_minutes > 30:
                        status = SessionStatus.IDLE
                
                session = Session(
                    session_id=account.get('id', 'unknown'),
                    user_id=identity_id,
                    username=username,
                    app_type=app_type,
                    app_name=app_name,
                    status=status,
                    created_at=created_at or datetime.now(),
                    last_activity=last_activity,
                    metadata=account,
                )
                sessions.append(session)
            
            active = [s for s in sessions if s.status == SessionStatus.ACTIVE]
            idle = [s for s in sessions if s.status == SessionStatus.IDLE]
            
            return UserSessions(
                user_id=identity_id,
                username=username,
                sailpoint_identity_id=identity_id,
                total_sessions=len(sessions),
                active_sessions=active,
                idle_sessions=idle,
            )
        except Exception as e:
            logger.error(f"Failed to get user sessions: {e}")
            return None
    
    @staticmethod
    def _detect_app_type(app_name: str) -> AppType:
        """Detect app type from application name."""
        app_lower = app_name.lower()
        if 'google' in app_lower or 'workspace' in app_lower:
            return AppType.GOOGLE_WORKSPACE
        elif 'okta' in app_lower:
            return AppType.OKTA
        elif 'aws' in app_lower:
            return AppType.AWS
        elif 'slack' in app_lower:
            return AppType.SLACK
        return AppType.GENERIC
    
    @staticmethod
    def _parse_date(date_str: Optional[str]) -> Optional[datetime]:
        """Parse ISO datetime string."""
        if not date_str:
            return None
        try:
            return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except Exception:
            return None
