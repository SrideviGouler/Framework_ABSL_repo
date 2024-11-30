import time
import pytest
from selenium import webdriver


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

@pytest.fixture()
def launching_driver():
    driver=webdriver.Chrome(options=opts)
    driver.get("https://leappreprod.adityabirlasunlifeinsurance.com/preprod/#/login")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    # driver.close()