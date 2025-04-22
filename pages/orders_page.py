from locators.orders_locators import OrdersLocators
from pages.core_page import CorePage
import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class OrdersPage(CorePage):
    @allure.step('Wait for orders feed link')
    def wait_orders_feed(self):
        self.wait_for_visible(OrdersLocators.ORDERS_FEED_LINK, timeout=15)

    @allure.step('Click orders feed link')
    def click_orders_feed(self):
        self.wait_for_clickable(OrdersLocators.ORDERS_FEED_LINK, timeout=15)
        self.perform_click(OrdersLocators.ORDERS_FEED_LINK)

    @allure.step('Click order in feed')
    def click_feed_order(self):
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(OrdersLocators.ORDER_ITEM)
        )
        self.perform_click(OrdersLocators.ORDER_ITEM)

    @allure.step('Verify order details modal')
    def verify_order_details(self):
        return self.is_element_visible(OrdersLocators.ORDER_DETAILS_MODAL)

    @allure.step('Drag ingredient to burger area')
    def move_ingredient_to_burger(self):
        source = self.wait_for_visible(OrdersLocators.BUN_ITEM, timeout=15)
        target = self.wait_for_visible(OrdersLocators.BURGER_DROP_AREA, timeout=15)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", source)
        self.drag_and_drop_element(source, target)
        time.sleep(1)  # Wait for UI update

    @allure.step('Wait for burger area')
    def wait_burger_area(self):
        self.wait_for_clickable(OrdersLocators.BURGER_DROP_AREA, timeout=20)

    @allure.step('Sign in to account')
    def sign_in(self, user_data):
        credentials, _, status_code = user_data
        if status_code != 200:
            raise ValueError(f"User creation failed with status {status_code}")
        email = credentials["email"]
        password = credentials["password"]

        self.wait_for_clickable(OrdersLocators.PROFILE_LINK, timeout=15)
        self.perform_click(OrdersLocators.PROFILE_LINK)
        self.wait_for_visible(OrdersLocators.EMAIL_FIELD, timeout=15)
        self.input_text(OrdersLocators.EMAIL_FIELD, email)
        self.input_text(OrdersLocators.PASSWORD_FIELD, password)
        self.perform_click(OrdersLocators.SIGN_IN_BUTTON)
        time.sleep(2)  # Wait for login to complete

    @allure.step('Click place order button')
    def click_place_order(self):
        self.wait_for_clickable(OrdersLocators.PLACE_ORDER_BUTTON, timeout=15)
        self.perform_click(OrdersLocators.PLACE_ORDER_BUTTON)
        time.sleep(2)  # Wait for order processing

    @allure.step('Close order modal')
    def close_order_modal(self):
        self.wait_for_clickable(OrdersLocators.CLOSE_ORDER_MODAL, timeout=15)
        self.perform_click(OrdersLocators.CLOSE_ORDER_MODAL)
        time.sleep(1)

    @allure.step('Click profile link')
    def click_profile(self):
        self.wait_for_clickable(OrdersLocators.PROFILE_LINK, timeout=15)
        self.perform_click(OrdersLocators.PROFILE_LINK)

    @allure.step('Click order history link')
    def click_order_history(self):
        self.wait_for_clickable(OrdersLocators.ORDER_HISTORY_LINK, timeout=15)
        self.perform_click(OrdersLocators.ORDER_HISTORY_LINK)
        time.sleep(1)  # Wait for history page to load

    @allure.step('Get history order ID')
    def get_history_order_id(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(OrdersLocators.HISTORY_ORDER_ID)
        )
        return self.get_element_text(OrdersLocators.HISTORY_ORDER_ID).lstrip('0')

    @allure.step('Get feed order ID')
    def get_feed_order_id(self):
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(OrdersLocators.FEED_ORDER_ID)
        )
        return self.get_element_text(OrdersLocators.FEED_ORDER_ID).lstrip('0')

    @allure.step('Get total orders count')
    def get_total_orders(self):
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(OrdersLocators.TOTAL_ORDERS_COUNT)
        )
        return self.get_element_text(OrdersLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Get today orders count')
    def get_today_orders(self):
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(OrdersLocators.TODAY_ORDERS_COUNT)
        )
        return self.get_element_text(OrdersLocators.TODAY_ORDERS_COUNT)

    @allure.step('Click builder link')
    def click_builder(self):
        self.wait_for_clickable(OrdersLocators.BUILDER_LINK, timeout=15)
        self.perform_click(OrdersLocators.BUILDER_LINK)

    @allure.step('Get order ID after placement')
    def get_order_id(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(OrdersLocators.ORDER_ID_MODAL)
        )
        return self.get_element_text(OrdersLocators.ORDER_ID_MODAL).lstrip('0')

    @allure.step('Get in-progress order ID')
    def get_in_progress_order_id(self):
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(OrdersLocators.IN_PROGRESS_ORDER_ID)
        )
        return self.get_element_text(OrdersLocators.IN_PROGRESS_ORDER_ID).lstrip('0')