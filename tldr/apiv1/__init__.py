from flask import Blueprint, request
from logbook import Logger
import requests
from textrankr import TextRank


apiv1_module = Blueprint('apiv1', __name__, template_folder='templates')
log = Logger(__name__)


@apiv1_module.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    return summarize_text(text)


@apiv1_module.route('/summarize_url', methods=['POST'])
def summarize_url():
    url = request.form('url')
    text = requests.get(url)
    return summarize_text(text)


def summarize_text(text):
    import jpype
    jpype.attachThreadToJVM()
    textrank = TextRank(text)
    return textrank.summarize()
