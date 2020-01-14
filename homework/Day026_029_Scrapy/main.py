import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1578982344.A.43C.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1578986401.A.966.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='PTTCrawler.json')
    process.start()

if __name__ == '__main__':
    main()