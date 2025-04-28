from pages.reset_password_page import ResetPasswordPage
from config import Endpoints
import allure

class TestPasswordReset:
    @allure.title('Navigate to password recovery page')
    def test_navigate_to_recovery(self, browser):
        reset_page = ResetPasswordPage(browser)
        reset_page.click_profile()
        reset_page.wait_recovery_link()
        reset_page.click_recovery()
        assert reset_page.get_page_url() == Endpoints.PASSWORD_RECOVERY_PAGE

    @allure.title('Submit email for password recovery')
    def test_submit_recovery_email(self, browser, generate_user):
        reset_page = ResetPasswordPage(browser)
        user_data, _, _ = generate_user

        reset_page.click_profile()
        reset_page.wait_recovery_link()
        reset_page.click_recovery()
        reset_page.input_recovery_email(user_data['email'])
        reset_page.click_recover()
        reset_page.wait_save_button()

        assert reset_page.get_page_url() == Endpoints.PASSWORD_RESET_PAGE

    @allure.title('Toggle password visibility highlights field')
    def test_toggle_password_visibility(self, browser):
        reset_page = ResetPasswordPage(browser)
        reset_page.click_profile()
        reset_page.wait_recovery_link()
        reset_page.click_recovery()
        reset_page.click_recover()
        reset_page.toggle_password_visibility()

        assert reset_page.verify_active_password()