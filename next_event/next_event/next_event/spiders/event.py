import scrapy


class EventSpider(scrapy.Spider):
    name = "event"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/upcoming"]

    def parse(self, response):
        pass
