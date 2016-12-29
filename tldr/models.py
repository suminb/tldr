from bs4 import BeautifulSoup
from newspaper import fulltext

from tldr.utils import summarize_text


class Article(object):

    #: BeautifulSoup object
    soup = None

    _title = None
    _text = None
    _summary = None

    def __init__(self, html):
        self.html = html

    def init_soup(self):
        if self.soup is None:
            self.soup = BeautifulSoup(self.html, 'html.parser')
        return self.soup

    @property
    def published_at(self):
        raise NotImplementedError()

    @property
    def fetched_at(self):
        raise NotImplementedError()

    @property
    def title(self):
        if self._title is None:
            soup = self.init_soup()
            self._title = soup.title.get_text().strip()
        return self._title

    @property
    def url(self):
        raise NotImplementedError()

    @property
    def canonical_url(self):
        raise NotImplementedError()

    # TODO: Make @cached_property
    @property
    def text(self):
        """Extracts text body (an article) from HTML."""
        # FIXME: What's going to happen when no article is found?

        if self._text is None:
            self._text = fulltext(self.html, 'ko')
        return self._text

    @property
    def summary(self):
        if self._summary is None:
            self._summary = summarize_text(self.text)
        return self._summary

    def as_dict(self):
        keys = ['title', 'html', 'text', 'summary']
        return {key: getattr(self, key) for key in keys}
