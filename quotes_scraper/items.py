import scrapy

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birth_date = scrapy.Field()
    birth_place = scrapy.Field()
    description = scrapy.Field()
    