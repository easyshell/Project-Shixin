import json

from scrapy import Selector

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.http import Request

from shixin.items import *
from misc.log import *


class shixinSpider(Spider):
    name = "shixin"
    #download_delay = 2
    allowed_domains = ["shixin.court.gov.cn"]
    start_urls = [
        "http://shixin.court.gov.cn/personMore.do?currentPage=%d" % d for d in range(0, 69895, 1)
    ]


    def parse(self, response):
        x = Selector(response)
        raw_urls = x.xpath("//a/@id").extract()
        urls = []
        for url in raw_urls:
            url = 'http://shixin.court.gov.cn/detail?id=%s' % url
            urls.append(url)
        for url in urls:
            yield Request(url, callback=self.parse_detailed)


    def parse_detailed(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        items = []
        item = shixinItem()
        item["id"] = jsonresponse["id"]
        info('Processing id '+ str(jsonresponse["id"]))
        item["iname"] = jsonresponse["iname"]
        item["caseCode"] = jsonresponse["caseCode"]
        item["age"] = jsonresponse["age"]
        item["sexy"] = jsonresponse["sexy"]
        item["cardNum"] = jsonresponse["cardNum"]
        item["courtName"] = jsonresponse["courtName"]
        item["areaName"] = jsonresponse["areaName"]
        item["partyTypeName"] = jsonresponse["partyTypeName"]
        item["gistId"] = jsonresponse["gistId"]
        item["regDate"] = jsonresponse["regDate"]
        item["gistUnit"] = jsonresponse["gistUnit"]
        item["duty"] = jsonresponse["duty"]
        item["performance"] = jsonresponse["performance"]
        if "performedPart" in json.loads(response.body):
            item["performedPart"] = jsonresponse["performedPart"]
            item["unperformPart"] = jsonresponse["unperformPart"]
        else:
            item["performedPart"] = "NA"
            item["unperformPart"] = "NA"
        item["disruptTypeName"] = jsonresponse["disruptTypeName"]
        item["publishDate"] = jsonresponse["publishDate"]
        items.append(item)
        return items


    #def process_request(self, Request, shixinSpider):
        #info('process ' + str(Request))
        #return Request

