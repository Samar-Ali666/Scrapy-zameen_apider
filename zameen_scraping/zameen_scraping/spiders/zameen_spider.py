# -*- coding: utf-8 -*-
import scrapy
from ..items import ZameenScrapingItem


class ZameenSpiderSpider(scrapy.Spider):
    name = 'zameen'
    page_number = 2
    start_urls = [
        'https://www.zameen.com/Homes/Lahore_DHA_Defence-9-1.html'
    ]

    def parse(self, response):

        items = ZameenScrapingItem()

        all_article = response.css('li.ef447dde')

        for articles in all_article:

            location = articles.css('._162e6469::text').extract()

            area = articles.css('span.b6a29bc0 span::text').extract()

            beds = articles.css('span.b6a29bc0::text').extract()

            description = articles.css('h2.c0df3811::text').extract()

            price = articles.css('span.f343d9ce::text').extract()

            items['location'] = location
            items['area'] = area
            items['beds'] = beds
            items['description'] = description
            items['price'] = price

            yield items

        next_page = 'https://www.zameen.com/Homes/Lahore_DHA_Defence-9-' + \
            str(ZameenSpiderSpider.page_number) + '.html'

        if ZameenSpiderSpider.page_number <= 165:
            ZameenSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
