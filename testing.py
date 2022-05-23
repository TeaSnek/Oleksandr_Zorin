from multiprocessing.connection import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from black_magic import *
import time


if __name__ == '__main__':
    try:
        base = BasePage()
        base.go_to_site()
        main_page = MainPage()
        target = TargetPage()
        cart = CartPage()
        values = []
        wait = WebDriverWait(base.driver, 5)

        desired_username = 'ReVeSTri'
        main_page.set_username(desired_username)
        assert main_page.username == desired_username

        desired_password = 'asan124100'
        main_page.set_password(desired_password)
        assert main_page.password == desired_password

        prev_url = main_page.driver.current_url
        main_page.login_tab_toggle()
        curr_url = main_page.driver.current_url
        print(prev_url, curr_url)
        element = wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT_FIELD))

        main_page.put_username()
        assert True==True

        main_page.put_password()
        assert True==True

        main_page.click_login_button()
        element = wait.until(EC.invisibility_of_element(Locators.LOGIN_LINK))
        assert main_page.find_element((by.XPATH, '/html/body/nav/div[1]/ul/li[6]/a')).is_displayed() == True

        main_page.click_laptops_btn()
        wait.until(EC.element_to_be_clickable(Locators.TARGET_LP_BTN))
        assert main_page.find_element((Locators.TARGET_LP_BTN)).is_displayed() == True

        prev_url = main_page.driver.current_url
        main_page.click_target_btn()
        curr_url = main_page.driver.current_url
        assert prev_url != curr_url

        element = wait.until(EC.element_to_be_clickable(Locators.ADD_TC_BTN))
        target.click_add_btn()
        assert wait.until(EC.alert_is_present()) != None

        target.close_popup()
        assert wait.until_not(EC.alert_is_present()) != None

        prev_url = main_page.driver.current_url
        target.click_cart_btn()
        curr_url = main_page.driver.current_url
        assert prev_url != curr_url

        cart.click_order_btn()
        assert wait.until(EC.element_to_be_clickable(Locators.NAME_INPUT_FIELD)) != None
    
        for func, line in zip([cart.set_city, cart.set_country, cart.set_credit_card, cart.set_month, cart.set_year, cart.set_name ], 
                              ['Cherkassy', 'Ukraine', '8456 3365 7596 8542', 'May', '2022', 'Andrii Savonov']):
            func(line)
        for value, target_value in zip([cart.city, cart.country, cart.credit_card, cart.month, cart.year, cart.name ], 
                                       ['Cherkassy', 'Ukraine', '8456 3365 7596 8542', 'May', '2022', 'Andrii Savonov']):
            assert value == target_value

        cart.fill_form()
        for field, target_value in zip([Locators.NAME_INPUT_FIELD, Locators.COUNTRY_INPUT_FIELD, Locators.CITY_INPUT_FIELD, Locators.CREDIT_INPUT_FIELD, Locators.MONTH_FIELD, Locators.YEAR_FIELD],
                                       [cart.name, cart.country, cart.city, cart.credit_card, cart.month, cart.year]):
            assert cart.find_element(field).get_attribute('value') == target_value

        cart.buy_all()
        time.sleep(1)
        assert cart.check_for_pop_up_window()
        
        print('Hello World!')
    finally:
        base.driver.quit()