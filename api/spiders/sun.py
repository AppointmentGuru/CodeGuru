import scrapy

class SunICDCodeSpider(scrapy.Spider):
    name = 'sunicdcodespider'
    start_urls = ['http://www0.sun.ac.za/aotc/icd10/mf_icd10_codelist.php?start={}'.format(page) for page in range(1, 39032, 30)]

    def parse(self, response):
        for row in response.css('#tbl_mf_icd10_codelist tbody tr'):
            yield {
                'code': row.css('.mf_icd10_code_icd10_code span ::text').extract_first().strip(),
                'description': row.css('.mf_icd10_code_icd10_desc span ::text').extract_first().strip()
            }
