from selenium.webdriver.common.by import By
from POM.basepage import BasePage


host_url = "http://101.52.252.39/WEB/A0001/B0001/firstpage"

class SearchPage(BasePage):
    '''
    search_loc = (By.ID, "Sb_form_q")
    btn_loc = (By.ID, "Sb_form_q")
    '''

    def __init__(self, search_loc, btn_loc):
        # 调用父类构造方法
        super(SearchPage,self).__init__()
        if search_loc != False:
            self.search_loc = search_loc
        if search_loc != False:
            self.btn_loc = btn_loc

    def search_content(self, content):
        InputContent = self.find_element(*self.search_loc)
        InputContent.Send_keys(content)

    def clink(self):
        InputBtn = self.find_element(*self.btn_loc)
        InputBtn.click()

if __name__ == '__main__':
    searchpage = SearchPage(False, (By.ID, '//*[@id="navbarA"]/li[21]/a'))
    searchpage.open(host_url)
    searchpage.clink()
