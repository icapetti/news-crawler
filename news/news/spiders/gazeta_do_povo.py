import re
import json
from datetime import date, datetime

from scrapy.spiders import SitemapSpider

DATE = date.today()
BASE_URI = f"s3://da-vinci-raw/crawler-news/gazeta-do-povo/run={DATE}/"
SOURCE = "GAZETA DO POVO"

class GazetaDoPovoSpider(SitemapSpider):
    name = "gazeta_do_povo"
    allowed_domains = ['www.gazetadopovo.com.br']
    sitemap_urls = ['https://www.gazetadopovo.com.br/sitemap.xml']
    custom_settings = {"FEED_URI": BASE_URI +
                       "%(batch_id)d-gazeta_do_povo-%(batch_time)s.jl.gz", }
    rotate_user_agent = True

    def parse(self, response):
        if response.xpath("//ul[@class='publish-at']/li/text()").get():
            date = response.xpath("//ul[@class='publish-at']/li/text()").get()
        elif response.xpath("//ul[@class='wgt-date']/li/text()").get():
            for item in response.xpath("//ul[@class='wgt-date']/li/text()"):
                if re.match(r'(\d{2}).(\d{2}).(\d{2,4})', item.get()):
                    date = item.get()
                    break
        elif response.xpath("////script[@type='application/ld+json' and contains(text(), 'datePublished')]").get():
            raw_date = response.xpath(
                "////script[@type='application/ld+json' and contains(text(), 'datePublished')]").get()
            date = json.loads(
                raw_date.replace(
                    '<script type="application/ld+json">',
                    '').replace(
                    '</script>',
                    ''))["datePublished"]
        else:
            date = None

        content = ""
        for p in response.xpath("//p[@tabindex=0]").extract():
            content = content + p

        content = re.sub(r"\s", " ", content)
        regex = r"(?<=>)((?!\s*<)[\s\S]+?)(?=<)"
        content = "".join(re.findall(regex, content)).replace(" ", "")

        if response.xpath("//meta[@name='author']/content").get():
            author = response.xpath(
                "//meta[@name='author']/content/text()").get()
        elif response.xpath("//span[@class='author-name']/text()").get():
            author = response.xpath(
                "//span[@class='author-name']/text()").get()
        elif response.xpath("//a[@class='gtm-link-autor author-name-link']/text()").get():
            author = response.xpath(
                "//a[@class='gtm-link-autor author-name-link']/text()").get()
        elif response.xpath("//div[@class='post-caption']/span/text()").get():
            author = response.xpath(
                "//div[@class='post-caption']/span/text()").get()
        else:
            author = None

        if response.xpath("//title/text()").get():
            title = response.xpath("//title/text()").get()
        elif response.xpath("//h1[@class='post-title']/span/text()").get():
            title = response.xpath(
                "//h1[@class='post-title']/span/text()").get()
        else:
            title = None

        yield {
            "date": date,
            "content": content,
            "author": author,
            "title": title,
            "source": SOURCE,
            "url": response.url,
            "created_at": datetime.now()
        }
