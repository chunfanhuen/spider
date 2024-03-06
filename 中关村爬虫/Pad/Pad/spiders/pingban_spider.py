import scrapy
import requests
from ..items import PadItem


# /html/body/div[4]/div[1]/div[8]/div[3] /html/body/div[4]/div[1]/div[8]/div[4] /html/body/div[4]/div[1]/div[8]/div[6]
# /html/body/div[4]/div[1]/div[8]/div[4]/div[2]/ul/li[1]/div[1]/span/a
# /html/body/div[4]/div[1]/div[8]/div[3]/div[2]/ul/li[1]/div[1]/span/a/text()
#/html/body/div[4]/div[1]/div[8]/div[3]/div[2]/h3/a /html/body/div[4]/div[1]/div[8]/div[4]/div[2]/h3/a
# /html/body/div[4]/div[1]/div[8]/div[3]/div[3]/span[1]/b[2]
#
#


class PingbanSpiderSpider(scrapy.Spider):
    name = "pingban_spider"
    allowed_domains = ["www.zol.com.cn"]
    start_urls = ["https://detail.zol.com.cn/tablepc/"]

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[1]/div[8]/div')
        for li in li_list:
            suoshu = li.xpath('./div[2]/ul/li[1]/div[1]/span/a/text()').extract()
            name = li.xpath('./div[2]/h3/a/text()').extract()
            date = li.xpath('./div[3]/span[2]/text()').extract()
            price = li.xpath('./div[3]/span[1]/b[2]/text()').extract()
            system = li.xpath('./div[2]/ul/li[3]/text()').extract()
            screen = li.xpath('./div[2]/ul/li[2]/text()').extract()
            comment = li.xpath('./div[2]/div/div[1]/span/a/text()').extract()
            fen = li.xpath('./div[2]/div/div[1]/b/text()').extract()
            # name = name[0]
            # suoshu = suoshu[0]
            # date = date[0]
            # price = price[0]
            # system = system[1]
            # screen = screen[1]
            # comment = comment[0]
            # 评分 = 评分[0]
            print(suoshu)
            print(name)
            print(date)
            print(price)
            print(system)
            print(screen)
            print(comment)
            print(fen)
        pass
