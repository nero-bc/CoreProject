import httpx
from selectolax.parser import HTMLParser


class SitemapBuilder:
    def __init__(self, url: str) -> None:
        self.url = url

    @staticmethod
    def get_parser(xml: str) -> HTMLParser:
        return HTMLParser(xml)

    @staticmethod
    def get_content_given_url(url: str) -> str:
        return httpx.get(url).content

    def get_links_from_sitemap(self, url: str) -> list[str]:
        sitemap_content = self.get_content_given_url(url)
        sitemap_parser = self.get_parser(sitemap_content)

        loc_nodes = sitemap_parser.select("loc").matches
        links = [node.text() for node in loc_nodes]
        return links

    def build(self):
        index_sitemap_links = self.get_links_from_sitemap(self.url)

        sitemap_link_buffer = []
        for sitemap in index_sitemap_links:
            individual_sitemap_link = self.get_links_from_sitemap(sitemap)
            sitemap_link_buffer.extend(individual_sitemap_link)

        print(sitemap_link_buffer)