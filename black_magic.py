from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Locators:
    LOGIN_LINK = [by.XPATH, '/html/body/nav/div[1]/ul/li[5]/a']
    USERNAME_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input']
    PASSWORD_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input']
    LOGIN_BTN = [by.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]']
    LAPTOPS_BTN = [by.XPATH, '/html/body/div[5]/div/div[1]/div/a[3]']
    TARGET_LP_BTN = [by.LINK_TEXT, 'Dell i7 8gb']
    ADD_TC_BTN = [by.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a']
    CART_BTN = [by.XPATH, '/html/body/nav/div/div/ul/li[4]/a']
    ORDER_BTN = [by.XPATH, '/html/body/div[6]/div/div[2]/button']
    NAME_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input']
    COUNTRY_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input']
    CITY_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/input']
    CREDIT_INPUT_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[4]/input']
    MONTH_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[5]/input']
    YEAR_FIELD = [by.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[6]/input']
    PURCHASE_BTN = [by.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]']
    OK_BTN = [by.LINK_TEXT, 'OK']

class Results():
    res_good = 'found'
    res_bad = 'not_found'

class BasePage:
    def __init__(self, driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))):
        self.driver = driver
        driver.maximize_window()
        self.base_url = 'https://www.demoblaze.com/index.html'

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def go_to_site(self):
        return self.driver.get(self.base_url)

        
class MainPage(BasePage):
    username = None
    password = None

    def set_username(self, username):
        self.username = username
        
    def set_password(self, password):
        self.password = password

    def login_tab_toggle(self):
        login_tab_tog = self.find_element(Locators.LOGIN_LINK)
        login_tab_tog.click()

    def put_username(self):
        username_field = self.find_element(Locators.USERNAME_INPUT_FIELD)
        username_field.click()
        username_field.send_keys(self.username)

    def put_password(self):
        password_field = self.find_element(Locators.PASSWORD_INPUT_FIELD)
        password_field.click()
        password_field.send_keys(self.password)

    def click_login_button(self):
        login_btn = self.find_element(Locators.LOGIN_BTN)
        login_btn.click()
        return login_btn
    
    def click_laptops_btn(self):
        laptops_btn = self.find_element(Locators.LAPTOPS_BTN)
        laptops_btn.click()
        return laptops_btn
    
    def click_target_btn(self):
        target_btn = self.find_element(Locators.TARGET_LP_BTN)
        target_btn.click()
        return target_btn

class TargetPage(BasePage):
    def click_add_btn(self):
        add_btn = self.find_element(Locators.ADD_TC_BTN)
        add_btn.click()
        return add_btn

    def close_popup(self):
        popup = self.driver.switch_to.alert
        popup.accept()
        return popup

    def click_cart_btn(self):
        cart_btn = self.find_element(Locators.CART_BTN)
        cart_btn.click()
        return cart_btn

class CartPage(BasePage):
    name = None
    country = None
    city = None
    credit_card = None
    month = None
    year = None

    def click_order_btn(self):
        order_btn = self.find_element(Locators.ORDER_BTN)
        order_btn.click()
        return order_btn
    
    def set_name(self, name):
        self.name = name
    
    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

    def set_month(self, month):
        self.month = month

    def set_year(self, year):
        self.year = year

    def fill_form(self):
        active_field=self.find_element(Locators.NAME_INPUT_FIELD)
        active_field.click()
        active_field.send_keys(self.name)
        active_field=self.find_element(Locators.COUNTRY_INPUT_FIELD)
        active_field.click()
        active_field.send_keys(self.country)
        active_field=self.find_element(Locators.CITY_INPUT_FIELD)
        active_field.click()
        active_field.send_keys(self.city)
        active_field=self.find_element(Locators.CREDIT_INPUT_FIELD)
        active_field.click()
        active_field.send_keys(self.credit_card)
        active_field=self.find_element(Locators.MONTH_FIELD)
        active_field.click()
        active_field.send_keys(self.month)
        active_field=self.find_element(Locators.YEAR_FIELD)
        active_field.click()
        active_field.send_keys(self.year)
    
    def buy_all(self):
        buy_btn = self.find_element(Locators.PURCHASE_BTN)
        buy_btn.click()
        return buy_btn

    def check_for_pop_up_window(self):
        if "Thank you for your purchase!" in self.driver.page_source:
            time.sleep(1)
            self.driver.close()
            self.driver.quit()
            return True
        else:
            return False
            
    def buy_confirm(self):
        ok_btn = self.find_element(Locators.OK_BTN)
        ok_btn.click()
    




