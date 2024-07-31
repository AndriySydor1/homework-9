import json
from quotes_scraper.items import QuoteItem, AuthorItem

class QuotesScraperPipeline:
    def open_spider(self, spider):
        self.quotes_file = open('quotes.json', 'w')
        self.authors_file = open('authors.json', 'w')
        self.quotes_file.write('[')
        self.authors_file.write('[')
        self.first_quote = True
        self.first_author = True

    def close_spider(self, spider):
        self.quotes_file.write(']')
        self.authors_file.write(']')
        self.quotes_file.close()
        self.authors_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        if isinstance(item, QuoteItem):
            if self.first_quote:
                self.first_quote = False
            else:
                self.quotes_file.write(',')
            self.quotes_file.write(line)
        elif isinstance(item, AuthorItem):
            if self.first_author:
                self.first_author = False
            else:
                self.authors_file.write(',')
            self.authors_file.write(line)
        return item
    
    
    