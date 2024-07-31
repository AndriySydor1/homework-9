from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        **get_project_settings(),
        "FEEDS": {
            "quotes.json": {"format": "json"},
            "authors.json": {"format": "json"},
        },
    })

    process.crawl('quotes')
    process.start()
    