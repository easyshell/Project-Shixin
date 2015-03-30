# Scrapy settings for shixin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
# -*-coding:utf-8-*-

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)
from misc.log import *

BOT_NAME = 'shixin'

SPIDER_MODULES = ['shixin.spiders']
NEWSPIDER_MODULE = 'shixin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shixin (+http://www.yourdomain.com)'

#use new useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'shixin.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
    }

ITEM_PIPELINES = {
    #'shixin.pipelines.JsonWithEncodingPipeline': 300,
    #'shixin.pipelines.RedisPipeline': 301,
    'shixin.pipelines.CSVPipeline': 300
}

COOKIES_ENABLES=False

LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 0
