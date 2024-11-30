from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sales_details:
    def __init__(self,driver):
        self.driver = driver


    def enter_mbl_num(self):
        try:
          self.driver.find_element("xpath","//input[@id='mobileNumber']").send_keys("9960066619")
        except Exception as e:
            raise Exception(f"Error entering mobile number:{str(e)}")

    def clk_fetch_details(self):
        try:
            self.driver.find_element("xpath","//button[@name='Fetch Details']").click()
        except Exception as e:
            raise Exception(f"Error clicking fetch details:{str(e)}")

    def clk_ok_btn(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(("xpath", "//span[text()='OK']")))
            self.driver.find_element("xpath","//span[text()='OK']").click()
        except Exception as e:
            raise Exception(f"Error clicking ok button:{str(e)}")
