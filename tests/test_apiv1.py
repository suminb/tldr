import os

import pytest


def test_extract_text(testapp):
    html = '<html><body><p>Some text</p></body></html>'
    resp = testapp.post('/api/v1/extract-text', data={'html': html})
    assert resp.status_code == 200
    assert resp.data.decode('utf-8') == 'Some text'


@pytest.mark.parametrize('filename, start, end', [
    ('go-resolutions.html',
     'My Go Resolutions for 2017',
     'I understand the solution space better.')
])
def test_extract_test_long(testapp, filename, start, end):
    path = os.path.join('tests', 'samples', 'test_apiv1', filename)
    with open(path) as fin:
        html = fin.read()

    resp = testapp.post('/api/v1/extract-text', data={'html': html})
    assert resp.status_code == 200

    text = resp.data.decode('utf-8')
    assert text.startswith(start)
    assert text.endswith(end)


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
