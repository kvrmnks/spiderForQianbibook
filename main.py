from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class SpiderForQianbibook(object):
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.text = []

    def start(self, url):
        self.driver.get(url)
        elements = self.driver.find_elements_by_xpath("//ul[@id='chapterList']/li/a")
        length = len(elements)
        # length = 10
        for i in range(length):
            print(i, length)
            self.text.append(elements[i].text+"\n")
            elements[i].click()
            self.doOnePage()
            self.driver.back()
            elements = self.driver.find_elements_by_xpath("//ul[@id='chapterList']/li/a")

    def doOnePage(self):
        rds = self.driver.find_elements_by_class_name('rd')
        self.text.append(rds[0].text)
        # print(rds[0].text)
        pass

    def save(self, url):
        f = open(url, 'w', encoding="UTF-8")
        for x in self.text:
            f.write(x+'\n')
        f.close()


if __name__ == "__main__":
    a = SpiderForQianbibook()
    a.start('http://www.qianbibook.com/list/456/')
    a.save("1.txt")
