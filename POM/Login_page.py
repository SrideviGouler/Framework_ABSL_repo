class Login:
    def __init__(self,driver):
        self.driver = driver

    def login_id(self):
        try:
            self.driver.find_element("xpath","//input[@id='loginId']").send_keys("IN076761")
        except Exception as e:
            raise Exception(f"Error login ID: {str(e)}")

    def password(self):
        try:
            self.driver.find_element("xpath","//input[@id='password']").send_keys("str")
        except Exception as e:
            raise Exception(f"Error password: {str(e)}")

    def btn_login(self):
        try:
            self.driver.find_element("xpath","//button[@name='LOGIN']").click()
        except Exception as e:
            raise Exception(f"Error btn_login: {str(e)}")

    def clk_new_btn(self):
        try:
            self.driver.find_element("xpath","//div[text()='NEW APPLICATION']").click()
        except Exception as e:
            raise Exception(f"Error clk_new_item: {str(e)}")
