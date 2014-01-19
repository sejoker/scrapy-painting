from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import PaintItem
from scrapy.http import Request

class PaintSpider(Spider):
    name = "paint"
    allowed_domains = ["art-on-line.com.ua"]
    start_urls = ["http://art-on-line.com.ua/ru/8-zhanrovaya-zhivopis"]

    def complete_url(string):
        """Return complete url"""
        return "http://art-on-line.com.ua" + string

    def parse(self, response):
        hxs = Selector(response)
        # HXS to find url that goes to detail page
        items = hxs.xpath('//*[contains(@class, "product_list_details_left")]/h5/a/@href')

        for item in items:
            link = item.extract()
            yield Request(link, callback=self.parse_paint)

        next = hxs.xpath('//*[@id="pagination-next"]/a/@href')
        for item in next:
            link = item.extract()
            yield Request("http://art-on-line.com.ua" + link, callback=self.parse)

    def parse_paint(self, response):
        sel = Selector(response)        
        item = PaintItem()
        for title, price, author, width, height, status, rating, paintType, material in zip(sel.xpath('//*[@id="pb-right-column"]/h1/text()').extract(),
        						  	  sel.xpath('//*[@id="our_price_display"]/text()').extract(),
        						  	  sel.xpath('//*[@id="short_description_blockm"]/table/tr[1]/td[1]/a/text()').extract(),
        						  	  sel.xpath('//*[@id="idTab2"]/li[1]/span[2]/strong/text()').extract(),
                                      sel.xpath('//*[@id="idTab2"]/li[2]/span[2]/strong/text()').extract(),
        						  	  sel.xpath('//*[@id="idTab2"]/li[5]/span[2]/text()').extract(),
                                      sel.xpath('//*[contains(@class,"current-rating")]/text()').extract(),
                                      sel.xpath('//*[@id="idTab2"]/li[4]/span[2]/text()').extract(),
                                      sel.xpath('//*[@id="idTab2"]/li[3]/span[2]/text()').extract()):
        	item['title'] = title
        	item['price'] = price
        	item['width'] = width
                item['height'] = height
        	item['status'] = status
        	item['author'] = author
                item['rating'] = rating
                item['paintType'] = paintType
                item['material'] = material
                item['url'] = response.url
           	yield item