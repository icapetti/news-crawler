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
