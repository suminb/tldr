import jpype
from textrankr import TextRank


def summarize_text(text):
    jpype.attachThreadToJVM()
    textrank = TextRank(text)
    return textrank.summarize()
