# Scrapy settings for news project

import json
import os
from pathlib import Path
from random import choice
from dotenv import load_dotenv

# Loads variables on the .env file to the local environment variables
# Add your aws credentials on the .env file
user = os.environ.get("USER") if os.environ.get("USER") else os.environ.get("USERNAME")
load_dotenv(f'/home/{user}/.credentials/.env')

PROJECT_BASE_PATH = Path(__file__).resolve().parents[1]

BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'

# LOG Level
LOG_ENABLED = True
LOG_LEVEL = 'INFO'

# CREDENTIALS FOR S3
AWS_ACCESS_KEY_ID = os.getenv("aws_id")
AWS_SECRET_ACCESS_KEY = os.getenv("aws_secret")

# FEED compressed jsonlines
FEED_EXPORTERS = {
    'jl.gz': 'news.exporters.JsonLinesGzipItemExporter',
}
FEED_FORMAT = 'jl.gz'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_BATCH_ITEM_COUNT = 2000

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.3

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'news.pipelines.S3Pipeline': 300,
   'news.pipelines.ScreenshotPipeline': 400,
}

USER_AGENT = choice([
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2483.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240", 
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
])
