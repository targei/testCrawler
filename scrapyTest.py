# download twisted from
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
# pip install Twisted-18.9.0-cp37-cp37m-win_amd64.whl
# pip install scrapy

#scrapy runspider myspider.py


import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
EOF