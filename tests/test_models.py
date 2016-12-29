# import pytest

from tldr.models import Article


def test_canonical_url():
    html = """
        <html>
            <head>
                <link rel="canonical" href="https://techcrunch.com/2016/12/22/aws-catapulted-amazon-into-a-breakout-2016-on-wall-street/" />
            </head>
        </html>
    """  # noqa
    article = Article(html)
    assert article.canonical_url == 'https://techcrunch.com/2016/12/22/aws-catapulted-amazon-into-a-breakout-2016-on-wall-street/'  # noqa


# def test_canonical_url_not_found():
#     article = Article('')
#     with pytest.raises(ValueError):
#         article.canonical_url
