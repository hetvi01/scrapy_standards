import scrapy as scrapy

from ..items import QuoteWebsiteItem, QuoteWebsiteItem1


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # start_urls = ["https://quotes.toscrape.com/"]

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        # print(response)
        """
        If you’re a long-time Scrapy user, you’re probably familiar with .extract() and .extract_first() selector methods.
        Many blog posts and tutorials are using them as well. These methods are still supported by Scrapy,
        there are no plans to deprecate them.
        However, Scrapy usage docs are now written using .get() and .getall() methods.
        We feel that these new methods result in a more concise and readable code.
        """
        items = QuoteWebsiteItem()
        all_quotes = response.css('div.quote')
        for quote in all_quotes:
            items['title'] = quote.css("div span.text::text").getall()
            items['author'] = quote.css(".author::text").getall()
            items['tags'] = quote.css(".tags a::text").getall()
            items['tag_links'] = quote.css(".tags a::attr(href)").getall()  # return all links
            # items['tag_links1'] = quote.css(".tags a").attrib[
            #                           'href'] or "jkjjjjjj"  # return only first link throw error if not found
            # page 3



            # title = quote.xpath("./span[@class='text']/text()").get()
            # print(type(quote), "qiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            # title = quote.xpath("span").get()
            # print(title, "title")
            # author = quote.xpath()

            # tags = quote.xpath(".//a[@class='tag']")
            # print(tags)
            # tag_link = tags.xpath("@href")
            # tag_name = tags.xpath("text()")
            # print(tag_name.get())
            #
            # tag_name = quote.xpath(".//a[@class='tag']/text()").getall()
            # tag_links = quote.xpath(".//a[@class='tag']/@href").getall()
            # tag_data = dict(zip(tag_name, tag_links))
            # print(title, author, tag_name, tag_data)

            # items1['title1'] = quote.xpath(".//span[@class='text']/text()")
            # # items1['title1'] = quote.xpath(".//span[@class='text']/text()").get()
            # items1['author1'] = quote.css(".author::text").extract()
            # items1['tags1'] = quote.css(".tags a::text").extract()
            # items1['tag_links1'] = quote.css(".tags a::attr(href)").extract()  # return all links
            # items1['tag_links11'] = quote.css(".tags a").attrib['href']  # return only first link
            yield items

        # go to next page
        if next_page := response.css("li.next a::attr(href)").extract_first():
            yield response.follow(next_page, callback=self.parse)
