from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium. webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception:
            raise NameError("please install chorme")

    def open(self, url):
        if url != '':
            self.driver.get(url)
            self.driver.maxmize_window()

        else:
            raise ValueError("please imput url")

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception:
            print('%s页面没有找到%s元素' % (self, loc))

    def send_keys(self, loc, value, clear_first=True, click_first = True):
        try:

            if click_first:
                self.find_element(*loc).click()
            if clear_first :
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('%s页面没有找到%s元素' % (self, loc))


    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    basepage = BasePage()
    basepage.open("http://101.52.252.39/WEB/A0001/B0001/firstpage")




