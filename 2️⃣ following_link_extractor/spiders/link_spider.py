import scrapy
from following_link_extractor.items import FollowingLinkExtractorItem

class LinkSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["example.com"]  # Change to the target domain
    start_urls = ["https://example.com/"]  # Replace with educational/demo URL

    def parse(self, response):
        # Extract all links
        links = response.xpath('//a/@href').getall()
        for link in set(links):  # Remove duplicates
            item = FollowingLinkExtractorItem()
            item['url'] = response.urljoin(link)
            item['anchor_text'] = response.xpath(f'//a[@href="{link}"]/text()').get()
            yield item

            # Optionally follow the link (demo)
            if link.startswith("/"):
                yield response.follow(link, callback=self.parse)
