import scrapy


class QuotesSpider(scrapy.Spider):
    name = "mobiles"

    def start_requests(self):
        urls = [
            'https://www.amazon.in/s?k=mobile',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        container = response.css("li div.a-spacing-small a::attr(title)").getall()
        prices = response.css("li span.s-price::text").getall()
        Rating = response.css("li span.a-icon-alt::text").getall()
        for i in range(len(container)):
            name = container[i]
            price = prices[i]
            rating = Rating[i]
            yield {
            "Item":name,
            "Price":price,
            "Rating":rating,
            }
        # next_page_id = response.css("span.pagnLink a::attr(href)").get()
        # x = int(response.css("span.pagnLink a::text").get())
        # if(x <= 5):
        #     next_page = response.urljoin(next_page_id)
        #     yield scrapy.Request(next_page, callback=self.parse)
