import gzip

from scrapy.exporters import JsonLinesItemExporter


class JsonLinesGzipItemExporter(JsonLinesItemExporter):
    """
    SOURCE: https://github.com/scrapy/scrapy/issues/2174#issuecomment-283259507

    To use it, add

        FEED_EXPORTERS = {
            'jl.gz': 'myproject.exporters.JsonLinesGzipItemExporter',
        }
        FEED_FORMAT = 'jl.gz'

    to settings.py
    """

    def __init__(self, file, **kwargs):
        gzfile = gzip.GzipFile(fileobj=file, mode="wb")
        super(JsonLinesGzipItemExporter, self).__init__(gzfile, **kwargs)

    def finish_exporting(self):
        self.file.close()
