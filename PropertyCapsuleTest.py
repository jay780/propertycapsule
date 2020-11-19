
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create a new Chrome session 
        inst.driver = webdriver.Chrome("/home/user/Downloads/chromedriver_linux64/chromedriver")
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        # navigate to the application home page
        inst.driver.get("https://www.propertycapsule.com/")

    
    def test_admin_login(inst):
        # check Enterprise Admin Login button on Home page and click
        submit = inst.driver.find_element_by_xpath("/html/body/header/div[3]/div[3]/a[1]")
        submit.click()
    
    def test_dealmaker_login(inst):
        # check Deal Maker Login button on Home page and click
        submit = inst.driver.find_element_by_link_text("Deal Maker Signup/Login")
        submit.click()
  
    def test_map_maker(inst):
        # check Map Maker link on Home page and click
        submit = inst.driver.find_element_by_id("market-btn")
        submit.click()

    
    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
           return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)
