from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Direct_Mareketing_details:
    def __init__(self,driver):
        self.driver = driver


    def enter_lead_id(self):
        try:
            # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located("Insurance Advisor No. 002465"))
            self.driver.find_element("xpath","//input[@name='caRefA']").send_keys("sridevigouleru")
        except Exception as e:
            raise Exception(f"Error entering lead id:{str(e)}")

    def enter_ca_ref_id(self):
        try:
            self.driver.find_element("xpath","//input[@name='caRefB']").send_keys("sridevigouler")
        except Exception as e:
            raise Exception(f"Error clicking fetch details:{str(e)}")

    def clk_continue_btn(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(("xpath", "//span[text()='Continue']")))
            self.driver.find_element("xpath","//span[text()='Continue']").click()
        except Exception as e:
            raise Exception(f"Error clicking continue button:{str(e)}")