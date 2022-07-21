import scrapy

#

class IndexSpider(scrapy.Spider):
    name = 'IndexSpider'
    url = "https://www.cnn.com/markets/fear-and-greed"

    def parse(self, reponse):
        for line in reponse.css('div.market-fng-indicator'):
            yield {
                'index value': line.css('.market-fng-indicator__name::text').extract_first()
            }

