import subprocess

def runSpider():
    spiderName = "coronaCrawler"
    subprocess.check_output(['scrapy', 'crawl', spiderName])
    