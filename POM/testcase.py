# coding=utf-8
import unittest
from POM.search import SearchPage
from time import sleep

class TestRun(unittest.TestCase):
    def setUP(self):
        self.url = 'http://cn.bing.com/'
        sleep(2)
        self.content='bela'
        self.BingSearch = SearchPage()
    def test_search(self):
        self.BingSearch.open(self.url)
        self.BingSearch.search_content(self.content)
        self.BingSearch.btn_click()
        self.BingSearch.quit()

if __name__ == "__main__":
    unittest.main()