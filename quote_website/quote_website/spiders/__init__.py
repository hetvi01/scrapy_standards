# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy as scrapy

from ..items import QuoteWebsiteItem, QuoteWebsiteItem1


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
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
            items['tag_links1'] = quote.css(".tags a").attrib['href']  # return only first link


            # title = quote.xpath("./span[@class='text']/text()").get()
            # print(type(quote), "qiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            # title = quote.xpath("span").get()
            # print(title, "title")
            # author = quote.xpath()
            #
            # body > div > div: nth - child(2) > div.col - md - 8 > div:nth - child(1) > span.text
            # / html / body / div / div[2] / div[1] / div[1] / span[1]
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

            # use of xpath
            # / html / body / div / div[2] / div[1] / div[1] / span[1]

            # items1['title1'] = quote.xpath(".//span[@class='text']/text()")
            # # items1['title1'] = quote.xpath(".//span[@class='text']/text()").get()
            # items1['author1'] = quote.css(".author::text").extract()
            # items1['tags1'] = quote.css(".tags a::text").extract()
            # items1['tag_links1'] = quote.css(".tags a::attr(href)").extract()  # return all links
            # items1['tag_links11'] = quote.css(".tags a").attrib['href']  # return only first link
            yield items
            # yield items1
