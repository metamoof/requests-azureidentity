from session import AzureIdentitySession

from azure.identity import DefaultAzureCredential

def default_session(scope: str) -> AzureIdentitySession: 
    """Retrieve an AzureIdentitySession with the given scope using azure.identity.DefaultAzureCredential
    """
    credential = DefaultAzureCredential()
    return AzureIdentitySession(credential, scope)
