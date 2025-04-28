from locators.profile_locators import ProfileLocators
from pages.core_page import CorePage
import allure

class ProfilePage(CorePage):
    @allure.step('Sign in to profile')
    def sign_in(self, user_data):
        credentials, _, _ = user_data
        email = credentials["email"]
        password = credentials["password"]

        self.perform_click(ProfileLocators.PROFILE_LINK)
        self.input_text(ProfileLocators.EMAIL_FIELD, email)
        self.input_text(ProfileLocators.PASSWORD_FIELD, password)
        self.perform_click(ProfileLocators.SIGN_IN_BUTTON)

    @allure.step('Wait for sign-in button')
    def wait_sign_in_button(self):
        self.wait_for_clickable(ProfileLocators.SIGN_IN_BUTTON)

    @allure.step('Click sign-in button')
    def click_sign_in(self):
        self.perform_click(ProfileLocators.SIGN_IN_BUTTON)

    @allure.step('Wait for profile link')
    def wait_profile_link(self):
        self.wait_for_clickable(ProfileLocators.PROFILE_LINK)

    @allure.step('Click profile link')
    def click_profile(self):
        self.perform_click(ProfileLocators.PROFILE_LINK)

    @allure.step('Wait for order history link')
    def wait_order_history(self):
        self.wait_for_clickable(ProfileLocators.ORDER_HISTORY_LINK)

    @allure.step('Click order history link')
    def click_order_history(self):
        self.perform_click(ProfileLocators.ORDER_HISTORY_LINK)

    @allure.step('Click logout button')
    def perform_logout(self):
        self.perform_click(ProfileLocators.LOGOUT_BUTTON)

    @allure.step('Get current page URL')
    def get_page_url(self):
        return self.get_current_url()