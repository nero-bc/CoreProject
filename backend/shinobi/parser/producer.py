# Code Owners : `horidesu`, `baseplate-admin`
# Licensed Under : AGPL-v3
import datetime
from typing import TypedDict

from dateutil import parser
from decorators.return_error_decorator import return_on_error
from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.string import StringHelper


class ProducerDictionary(TypedDict):
    mal_id: str
    name: str
    name_japanese: str
    established: datetime.datetime
    about: str


class ProducerParser:
    def __init__(self, html: str):
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @property
    @return_on_error("")
    def get_producer_url(self):
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    @property
    @return_on_error("")
    def get_producer_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_producer_url)

    @property
    @return_on_error("")
    def get_producer_name(self):
        node = self.parser.css_first("#contentWrapper > div:first-child > h1")
        return self.string_helper.cleanse(node.text())

    @property
    @return_on_error("")
    def get_producer_japanese_name(self):
        node = self.parser.select("span").text_contains("Japanese:")
        return self.string_helper.cleanse(node.matches[0].next.text())

    @property
    @return_on_error("")
    def get_producter_establish_date(self):
        node = self.parser.select("span").text_contains("Established:")
        string_date = self.string_helper.cleanse(node.matches[0].next.text())
        actual_date = parser.parse(string_date)
        return actual_date

    @property
    @return_on_error("")
    def get_producer_about(self):
        return self.parser.css_first(
            "#content > div:nth-of-type(1) div.spaceit_pad > span:not(.dark_text)"
        ).text()

    def build_dictionary(self) -> ProducerDictionary:
        dictionary: ProducerDictionary = {
            "mal_id": self.get_producer_id,
            "name": self.get_producer_name,
            "name_japanese": self.get_producer_japanese_name,
            "established": self.get_producter_establish_date,
            "about": self.get_producer_about,
        }
        return dictionary
