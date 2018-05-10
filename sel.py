from selenium import webdriver
from selenium.webdriver.support.ui import Select
import bs4 as bs
import time
import os

path_to_chromedriver = r'E:/Projects/PythonProjects/ghoster/chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url='http://ceomadhyapradesh.nic.in/FindPollingStation.aspx'
browser.get(url)
select_element = Select(browser.find_element_by_xpath('//*[@id="ddlDistrict"]'))
all_options = [o.get_attribute('innerHTML') for o in select_element.options]
k=len(select_element.options)
for a in range(0,k):
    select_element = Select(browser.find_element_by_xpath('//*[@id="ddlDistrict"]'))
    select_element.select_by_index(a)
    time.sleep(2)
    try:
        os.mkdir('E:\\Projects\\mp\\' + all_options[a].strip(' ').strip('\n'))
    except Exception as e:
        pass
    select_element1=Select(browser.find_element_by_xpath('//*[@id="ddlAssembly"]'))
    all_options1 = [o.get_attribute('innerHTML') for o in select_element1.options]
    l=len(select_element1.options)
    for m in range(1,l):
        select_element1 = Select(browser.find_element_by_xpath('//*[@id="ddlAssembly"]'))
        time.sleep(2)
        try:
            os.mkdir('E:\\Projects\\mp\\' + all_options[a].strip(' ').strip('\n')+'\\'+all_options1[m].strip(' ').strip('\n'))
        except Exception as e:
            pass
        select_element1.select_by_index(m)
        browser.find_element_by_xpath('//*[@id="btnSearch"]').click()
        time.sleep(4)
        tab=browser.find_element_by_xpath('//*[@id="grid"]/center/div')
        inn=tab.get_attribute('innerHTML')
        with open('E:\\Projects\\mp\\' + all_options[a].strip(' ').strip('\n')+'\\'+all_options1[m].strip(' ').strip('\n')+'\\table.html', 'w',encoding='utf-8') as f:
            f.write(inn)



#select_element.select_by_index(0)
