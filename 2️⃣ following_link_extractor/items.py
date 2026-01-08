import scrapy

class FollowingLinkExtractorItem(scrapy.Item):
    url = scrapy.Field()
    anchor_text = scrapy.Field()
