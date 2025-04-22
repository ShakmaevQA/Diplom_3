from locators.builder_locators import BuilderLocators
from pages.core_page import CorePage
import allure

class BuilderPage(CorePage):
    @allure.step('Wait for builder link')
    def wait_builder_link(self):
        self.wait_for_visible(BuilderLocators.BUILDER_LINK)

    @allure.step('Click builder link')
    def click_builder(self):
        self.perform_click(BuilderLocators.BUILDER_LINK)

    @allure.step('Click orders feed link')
    def click_orders_feed(self):
        self.perform_click(BuilderLocators.ORDERS_FEED_LINK)

    @allure.step('Verify orders feed title is displayed')
    def verify_orders_feed_title(self):
        return self.is_element_visible(BuilderLocators.ORDERS_FEED_TITLE)

    @allure.step('Click ingredient')
    def click_ingredient(self):
        element = self.wait_for_clickable(BuilderLocators.BUN_ITEM)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.perform_click(BuilderLocators.BUN_ITEM)

    @allure.step('Verify ingredient details modal')
    def verify_ingredient_details(self):
        return self.is_element_visible(BuilderLocators.BUN_DETAILS)

    @allure.step('Close ingredient modal')
    def close_modal(self):
        self.perform_click(BuilderLocators.CLOSE_MODAL)

    @allure.step('Wait for close modal button')
    def wait_modal_close(self):
        self.wait_for_clickable(BuilderLocators.CLOSE_MODAL)

    @allure.step('Verify modal is closed')
    def verify_modal_closed(self):
        return not self.is_element_visible(BuilderLocators.CLOSE_MODAL)

    @allure.step('Drag ingredient to burger area')
    def move_ingredient_to_burger(self):
        source = self.browser.find_element(*BuilderLocators.BUN_ITEM)
        target = self.browser.find_element(*BuilderLocators.BURGER_DROP_AREA)
        self.drag_and_drop_element(source, target)

    @allure.step('Get ingredient count')
    def get_ingredient_count(self):
        return self.get_element_text(BuilderLocators.BUN_COUNTER)

    @allure.step('Wait for bun item')
    def wait_bun_item(self):
        self.wait_for_clickable(BuilderLocators.BUN_ITEM)

    @allure.step('Sign in to account')
    def sign_in(self, user_data):
        credentials, _, _ = user_data
        email = credentials["email"]
        password = credentials["password"]

        self.perform_click(BuilderLocators.PROFILE_LINK)
        self.input_text(BuilderLocators.EMAIL_FIELD, email)
        self.input_text(BuilderLocators.PASSWORD_FIELD, password)
        self.perform_click(BuilderLocators.SIGN_IN_BUTTON)

    @allure.step('Place order')
    def place_order(self):
        self.perform_click(BuilderLocators.PLACE_ORDER_BUTTON)

    @allure.step('Verify order confirmation')
    def verify_order_confirmation(self):
        return self.is_element_visible(BuilderLocators.ORDER_CONFIRMATION)

    @allure.step('Get current page URL')
    def get_page_url(self):
        return self.get_current_url()