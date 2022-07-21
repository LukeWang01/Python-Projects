import scrapy

#

# class Test(scrapy.Spider):
#     name = 'Test'
#     url = "https://books.toscrape.com/"
#
#     def parse(self, response):
#         for price in response.css('div.product_price'):
#
#             yield {
#                 'data': price.css('.price_color::text')
#             }


class Test(scrapy.Spider):
    name = 'Test'
    url = "https://books.toscrape.com/"

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }
