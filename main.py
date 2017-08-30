# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2017/8/13 18:33'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
