#!/bin/sh
cd /home/zhwang/news-crawler/
scrapy crawl Naver -a start_date='2015-08-22' -a end_date='2015-08-22' -a check_date='2015-08-24'
