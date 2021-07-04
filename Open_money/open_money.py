

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://www.bing.com')
driver.maximize_window()
sleep(1)
driver.find_element_by_partial_link_text('学术').click()
sleep(1)
driver.back()
#driver.find_element_by_id('sb_form_q').send_keys('招银云创')
#driver.find_element_by_id('sb_form_go').click()


#
# class params:
#
#     banktype = ['cmb']
#     actnbr = ['a','b','c']
#     arecod = ['a','b']
#     velflg = ['','1','0']
#     velflg = ['','1','0']
#     accac = ['','a','c']
#     d = ['','a','c']
#
#     function getall(): 组合
#
#         list
#         for i in banktype:
#             for j in actobr:
#                 for a in are:
#                     list.add(param(i,j,a))
#
#     function post(param):
#         reuqest.post(url,param)
#         return xxxx
#
#     fun deal(allparams):
#         resultDics
#         for params in allparams:
#             result = post()
#             resultDics.add([params,result])
#         html.report(resultDics)


