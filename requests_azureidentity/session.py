import logging
import requests
import time

logger = logging.getLogger(__name__)

class AzureIdentitySession(requests.Session):
    def __init__(
        self,
        credential,
        scope,
        **kwargs,
    ):
        super(AzureIdentitySession, self).__init__(**kwargs)
        self.credential = credential
        self.scope = scope
        self._token = None

    @property
    def token(self):
        if not self._token or self._token.expires_on - time.time() < 300:
            logger.debug("Token nonexisten or expired, generating new token")
            self._token = self.credential.get_token(self.scope)
        return self._token.token

    def request(
        self, method, url, data=None, headers=None, withhold_token=False, **kwargs
    ):
        if headers is None:
            headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        logger.debug("Adding Azure Identity Bearer Token")

        return super(AzureIdentitySession, self).request(
            method, url, headers=headers, data=data, **kwargs
        )