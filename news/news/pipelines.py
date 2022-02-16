# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class S3Pipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('author') and adapter.get('content'):
            if adapter.get('author').lower() not in (
                "gazeta do povo",
                "tudoparaná",
                "resultado",
                "bom gourmet",
                "coluna do leitor",
                "globoesporte.com / globo.com",
                "gazeta do povo online",
                "globo online",
                "da redação"
            ):

                return item
        
        raise DropItem(f"Missing author or content in {item}")

import hashlib
from urllib.parse import quote

import scrapy
from itemadapter import ItemAdapter

class ScreenshotPipeline:
    """Pipeline that uses Splash to render screenshot of
    every Scrapy item."""

    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    async def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        encoded_item_url = quote(adapter["url"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url)
        response = await spider.crawler.engine.download(request, spider)

        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to file, filename will be hash of url.
        url = adapter["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = f"{url_hash}.png"
        with open(filename, "wb") as f:
            f.write(response.body)

        # Store filename in item.
        adapter["screenshot_filename"] = filename
        return item
