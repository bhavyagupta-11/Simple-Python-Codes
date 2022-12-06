import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    #generates and sends url for scraping
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_id = response.url.split("/")[-2]
        filename = "quotes-%s"%page_id
        
        #to save in a json format
        for q in response.css("div.quote"):
            text=q.css('span.text::text').get()
            author=q.css('small.author::text').get()
            tags=q.css('a.tag::text').getall()
            
            yield{
                'text':text,
                'author':author,
                'tags':tags,
            }

        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
            
        #scrapy crawl quotes -o all_quotes.json
        
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)