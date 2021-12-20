import requests_azureidentity
import requests


def test_default_credential():
    scope = "https://graph.microsoft.com/.default"
    url = "https://graph.microsoft.com/v1.0/me/messages"

    resp = requests.get(url)
    assert resp.status_code == 401

    session = requests_azureidentity.default_session(scope)
    resp = session.get(url)
    assert resp.status_code == 200

