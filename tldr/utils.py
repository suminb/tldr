from bs4 import BeautifulSoup
import jpype
from newspaper import fulltext
from textrankr import TextRank


TEXT_HTML_RATIO_THRESHOLD = 0.01


def extract_text(html):
    """Extracts text from raw HTML."""
    text = fulltext(html, 'ko')

    # NOTE: Is this an appropriate condition to check?
    if float(len(text)) / len(html) > TEXT_HTML_RATIO_THRESHOLD:
        return text

    soup = BeautifulSoup(html, 'html.parser')
    article_tag_text = extract_text_from_article_tag(soup)

    if len(article_tag_text) > len(text):
        return article_tag_text

    return text


def extract_text_from_article_tag(soup):
    article_tag = soup.find('article')
    if article_tag:
        return article_tag.text
    else:
        return ''


def summarize_text(text):
    jpype.attachThreadToJVM()
    textrank = TextRank(text)
    return textrank.summarize()
