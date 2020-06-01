# -*- coding: utf-8 -*-
import scrapy
import requests


class PdfSpider(scrapy.Spider):
    name = 'pdf'
    # allowed_domains = ['a.com']
    start_urls = ['https://about.muse.jhu.edu/resources/freeresourcescovid19/']
    def start_requests(self):
        tar = input('请输入目标')
        print(tar)
        for i in self.start_urls:
            pass


    def parse(self, response):
        pass