# coding:utf-8
import json
from scrapy import cmdline
from urllib import request
from bs4 import BeautifulSoup

#cmdline.execute("scrapy crawl IBMBadges_spider -o IBMBadges.json".split())
cmdline.execute("scrapy crawl IBMBadges_spider_v1 -o IBMBadges.json".split())
#cmdline.execute("scrapy crawl IBMBadges_spider_v2 -o IBMBadges.json".split())