import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Produtos () :
            url = "https://www.saucedemo.com/"

            def setup_method(self, method):
                        self.driver=webdriver.Chrome()
                        self.driver.implicitly_wait(10)

            def teardown_method(self, method):
                        self.driver.quit()
                                       
            def test_selProduto(self):
                         self.driver.get(self.url)    
                         self.driver.find_element(By.ID,"user-name").send_keys('standard_user')
                         self.driver.find_element(By.NAME,"password").send_keys("secret-sase")