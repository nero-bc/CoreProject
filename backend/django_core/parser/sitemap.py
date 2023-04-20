from selectolax.parser import HTMLParser

from utilities.regex import RegexHelper


class SitemapParser:
    def __init__(self, html: str) -> None:
        self.parser = self.get_parser(html)
        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @property
    def genres(self) -> list[int]:
        """
        Given : https://myanimelist.net/anime.php
        return all the urls that match genre query
        """
        genre_nodes = self.parser.css('a[href*="genre"]')
        link_ids = [
            int(self.regex_helper.get_id_from_url(node.attributes["href"]))
            for node in genre_nodes
        ]
        return sorted(link_ids)

    @property
    def characters(self) -> list[int]:
        pass