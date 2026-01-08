BOT_NAME = 'following_link_extractor'

SPIDER_MODULES = ['following_link_extractor.spiders']
NEWSPIDER_MODULE = 'following_link_extractor.spiders'

ROBOTSTXT_OBEY = False  # For educational/demo purpose only
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    'following_link_extractor.pipelines.FollowingLinkExtractorPipeline': 300,
}
