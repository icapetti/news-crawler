from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news.spiders.gazeta_do_povo import GazetaDoPovoSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(GazetaDoPovoSpider)
process.start()
