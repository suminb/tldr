import sys

from flask import Blueprint, jsonify, request
from logbook import Logger, StreamHandler
import requests

from tldr.models import Article
from tldr.utils import summarize_text


apiv1_module = Blueprint('apiv1', __name__, template_folder='templates')

log = Logger(__name__)
log.handlers.append(StreamHandler(sys.stdout, level='INFO'))


# TODO: Make this more generic
# TODO: Move elsewhere
def json_requested():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/plain'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/plain']


@apiv1_module.route('summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    return summarize_text(text)


@apiv1_module.route('summarize-url', methods=['POST'])
def summarize_url():
    url = request.form['url']

    log.info('Fetching url {}', url)
    html = fetch_url(url)

    article = Article(html)

    if json_requested():
        return jsonify(article.as_dict())
    else:
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        return article.summary, 200, headers


@apiv1_module.route('extract-text', methods=['POST'])
def extract_text():
    html = request.form['html']
    article = Article(html)
    try:
        return article.text
    except AttributeError:
        # NOTE: When a parsing error occurs, an AttributeError is raised.
        # We'll deal with this exception later.
        return ''


def fetch_url(url, params={}):
    resp = requests.get(url, params=params)
    try:
        return resp.content.decode('utf-8')
    except UnicodeDecodeError:
        return resp.content.decode('euc-kr')
