import pytest


@pytest.mark.parametrize('content_type', ['application/json', 'text/plain'])
def test_summarize_url(testapp, content_type):
    url = 'https://github.com/suminb/finance'
    headers = {'Accept': content_type}
    data = {'url': url}
    resp = testapp.post('/api/v1/summarize-url', data=data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers['Content-Type'].split(';')[0] == content_type
