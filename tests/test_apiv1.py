import pytest


def test_extract_text(testapp):
    html = '<html><body><p>Some text</p></body></html>'
    resp = testapp.post('/api/v1/extract-text', data={'html': html})
    assert resp.status_code == 200
    assert resp.data.decode('utf-8') == 'Some text'


def test_extract_test_long(testapp):
    with open('tests/samples/go-resolutions.html') as fin:
        html = fin.read()

    resp = testapp.post('/api/v1/extract-text', data={'html': html})
    assert resp.status_code == 200

    text = resp.data.decode('utf-8')
    assert text.startswith('My Go Resolutions for 2017')
    assert text.endswith('I understand the solution space better.')


# TODO: Need to test against longer text
def test_summarize_text(testapp):
    text = 'This is some sample text'
    resp = testapp.post('/api/v1/summarize', data={'text': text})
    assert resp.status_code == 200


@pytest.mark.parametrize('content_type', ['application/json', 'text/plain'])
def test_summarize_url(testapp, content_type):
    url = 'https://github.com/suminb/finance'
    headers = {'Accept': content_type}
    data = {'url': url}
    resp = testapp.post('/api/v1/summarize-url', data=data, headers=headers)
    assert resp.status_code == 200
    assert resp.headers['Content-Type'].split(';')[0] == content_type
