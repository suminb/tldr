import sys

# from bs4 import BeautifulSoup
from flask import Blueprint, request
from logbook import Logger, StreamHandler
from newspaper import fulltext
import requests
from textrankr import TextRank


apiv1_module = Blueprint('apiv1', __name__, template_folder='templates')

log = Logger(__name__)
log.handlers.append(StreamHandler(sys.stdout, level='INFO'))


@apiv1_module.route('summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    return summarize_text(text)


@apiv1_module.route('summarize-url', methods=['POST'])
def summarize_url():
    url = request.form['url']

    log.info('Fetching url {}', url)
    html = fetch_url(url)

    log.info('Extracting text from {}', url)
    text = __extract_text__(html)

    log.info('Summarizing text...')
    return summarize_text(text)


@apiv1_module.route('extract-text', methods=['POST'])
def extract_text():
    html = request.form['html']
    try:
        return __extract_text__(html)
    except AttributeError:
        # NOTE: When a parsing error occurs, an AttributeError is raised.
        # We'll deal with this exception later.
        return ''


def summarize_text(text):
    import jpype
    jpype.attachThreadToJVM()
    textrank = TextRank(text)
    return textrank.summarize()


def fetch_url(url, params={}):
    resp = requests.get(url, params=params)
    try:
        return resp.content.decode('utf-8')
    except UnicodeDecodeError:
        return resp.content.decode('euc-kr')


def __extract_text__(html):
    """Extracts text body (an article) from HTML."""
    # TODO: What's going to happen when no article is found?

    # soup = BeautifulSoup(html, 'html.parser')
    # return ' '.join([p.text for p in soup.find_all('p')])

    return fulltext(html, 'ko')
