import time
from time import sleep

from POM.Login_page import Login
from POM.Sales_page import Sales_details
from POM.Direct_Marketing_details_page import Direct_Mareketing_details

def test_login(launching_driver):
    d=Login(launching_driver)
    s = Sales_details(launching_driver)


    d.login_id()
    sleep(1)
    d.password()
    sleep(1)
    d.btn_login()
    sleep(2)
    d.clk_new_btn()
    sleep(2)

    s=Sales_details(launching_driver)
    sleep(1)
    s.enter_mbl_num()
    sleep(1)
    s.clk_fetch_details()
    sleep(10)
    s.clk_ok_btn()

    dm = Direct_Mareketing_details(launching_driver)
    time.sleep(2)
    dm.enter_lead_id()
    time.sleep(2)
    dm.enter_ca_ref_id()
    time.sleep(5)
    dm.clk_continue_btn()











