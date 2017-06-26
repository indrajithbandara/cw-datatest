# -*- coding: utf-8 -*-  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select  
from selenium.common.exceptions import NoSuchElementException  
from selenium.common.exceptions import NoAlertPresentException  
import unittest, time, re  
  
class Ticket(unittest.TestCase):  
    def setUp(self):  
        self.driver = webdriver.Firefox()  
        self.driver.implicitly_wait(5)  
        self.base_url = "https://kyfw.12306.cn/"  
        self.verificationErrors = []  
        self.accept_next_alert = True  
      
    def test_ticket(self):  
        driver = self.driver  
        driver.get(self.base_url)  
        time.sleep(60)  
          
        T381_1=[u'上海南',u'嘉兴',u'海宁',u'杭州东']  
        T381_2=[u'柳州',u'来宾',u'南宁',u'百色',u'田林']  
        T25_1=[u'上海南',u'松江',u'嘉兴',u'海宁',u'杭州东']  
        T25_2=[u'柳州',u'南宁东',u'南宁']  
        while 1:  
            print u"开始查询T381列车"  
            for ticket_start in T381_1:  
                try:  
                    for ticket_end in T381_2:  
                        driver.find_element_by_id("fromStationText").click()  
                        driver.find_element_by_id("fromStationText").clear()  
                        driver.find_element_by_id("fromStationText").send_keys(ticket_start)  
                        driver.find_element_by_id("citem_0").click()  
                        driver.find_element_by_id("toStationText").click()  
                        driver.find_element_by_id("toStationText").clear()  
                        driver.find_element_by_id("toStationText").send_keys(ticket_end)  
                        driver.find_element_by_id("citem_0").click()  
                        driver.find_element_by_id("query_ticket").click()  
                        time.sleep(1)  
                        text = driver.find_element_by_id("YW_550000T38121").text  
                        if text != u"无":  
                            print u"发现【%s】到【%s】的余票，请赶紧抢"%(ticket_start,ticket_end)  
                            time.sleep(10)  
                        else:  
                            print u"【%s】到【%s】的余票为0"%(ticket_start,ticket_end)  
                except:  
                    time.sleep(1)  
                    continue  
            print u"结束查询T381列车结束"  
  
            print u"开始查询T25列车"  
  
            for ticket_start in T25_1:  
                try:  
                    for ticket_end in T25_2:  
                        driver.find_element_by_id("fromStationText").click()  
                        driver.find_element_by_id("fromStationText").clear()  
                        driver.find_element_by_id("fromStationText").send_keys(ticket_start)  
                        driver.find_element_by_id("citem_0").click()  
                        driver.find_element_by_id("toStationText").click()  
                        driver.find_element_by_id("toStationText").clear()  
                        driver.find_element_by_id("toStationText").send_keys(ticket_end)  
                        driver.find_element_by_id("citem_0").click()  
                        driver.find_element_by_id("query_ticket").click()  
                        time.sleep(1)  
                        text = driver.find_element_by_id("YW_5500000T2521").text  
                        if text != u"无":  
                            print u"发现【%s】到【%s】的余票，请赶紧抢"%(ticket_start,ticket_end)  
                            time.sleep(30)  
                        else:  
                            print u"【%s】到【%s】的余票为0"%(ticket_start,ticket_end)  
                except:  
                    time.sleep(1)  
                    continue  
            print u"查询T25列车结束"  
      
    def is_element_present(self, how, what):  
        try: self.driver.find_element(by=how, value=what)  
        except NoSuchElementException, e: return False  
        return True  
      
    def is_alert_present(self):  
        try: self.driver.switch_to_alert()  
        except NoAlertPresentException, e: return False  
        return True  
      
    def close_alert_and_get_its_text(self):  
        try:  
            alert = self.driver.switch_to_alert()  
            alert_text = alert.text  
            if self.accept_next_alert:  
                alert.accept()  
            else:  
                alert.dismiss()  
            return alert_text  
        finally: self.accept_next_alert = True  
      
    def tearDown(self):  
        self.driver.quit()  
        self.assertEqual([], self.verificationErrors)  
  
if __name__ == "__main__":  
    unittest.main()  