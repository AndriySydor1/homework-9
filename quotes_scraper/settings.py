# Scrapy settings for quotes_scraper project
BOT_NAME = 'quotes_scraper'

SPIDER_MODULES = ['quotes_scraper.spiders']
NEWSPIDER_MODULE = 'quotes_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'quotes_scraper.pipelines.QuotesScraperPipeline': 300,
}

# Other settings (user-agent, download delay, etc.) can be added as needed
