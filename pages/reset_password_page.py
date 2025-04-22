from locators.reset_password_locators import ResetPasswordLocators
from pages.core_page import CorePage
import allure

class ResetPasswordPage(CorePage):
    @allure.step('Wait for recovery link')
    def wait_recovery_link(self):
        self.wait_for_visible(ResetPasswordLocators.RECOVERY_LINK)

    @allure.step('Click recovery link')
    def click_recovery(self):
        self.perform_click(ResetPasswordLocators.RECOVERY_LINK)

    @allure.step('Wait for email input')
    def wait_email_input(self):
        self.wait_for_visible(ResetPasswordLocators.EMAIL_INPUT)

    @allure.step('Enter email for recovery')
    def input_recovery_email(self, email):
        self.input_text(ResetPasswordLocators.EMAIL_INPUT, email)

    @allure.step('Click recover button')
    def click_recover(self):
        self.perform_click(ResetPasswordLocators.RECOVER_BUTTON)

    @allure.step('Wait for save button')
    def wait_save_button(self):
        return self.wait_for_visible(ResetPasswordLocators.SAVE_BUTTON)

    @allure.step('Click password toggle icon')
    def toggle_password_visibility(self):
        self.perform_click(ResetPasswordLocators.TOGGLE_PASSWORD)

    @allure.step('Verify active password field')
    def verify_active_password(self):
        return self.is_element_visible(ResetPasswordLocators.ACTIVE_PASSWORD_FIELD)

    @allure.step('Get current page URL')
    def get_page_url(self):
        return self.get_current_url()

    @allure.step('Wait for profile link')
    def wait_profile_link(self):
        self.wait_for_clickable(ResetPasswordLocators.PROFILE_LINK)

    @allure.step('Click profile link')
    def click_profile(self):
        self.perform_click(ResetPasswordLocators.PROFILE_LINK)