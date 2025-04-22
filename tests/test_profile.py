from pages.profile_page import ProfilePage
from config import Endpoints
import allure

class TestProfile:
    @allure.title('Navigate to profile page')
    def test_navigate_to_profile(self, browser, generate_user):
        profile = ProfilePage(browser)

        profile.wait_sign_in_button()
        profile.sign_in(generate_user)

        profile.wait_profile_link()
        profile.click_profile()

        profile.wait_order_history()

        assert profile.get_page_url() == Endpoints.PROFILE_PAGE

    @allure.title('Access order history')
    def test_access_order_history(self, browser, generate_user):
        profile = ProfilePage(browser)

        profile.wait_sign_in_button()
        profile.sign_in(generate_user)

        profile.wait_profile_link()
        profile.click_profile()

        profile.wait_order_history()
        profile.click_order_history()

        assert profile.get_page_url() == Endpoints.ORDERS_PAGE

    @allure.title('Logout from profile')
    def test_logout(self, browser, generate_user):
        profile = ProfilePage(browser)

        profile.wait_sign_in_button()
        profile.sign_in(generate_user)

        profile.wait_profile_link()
        profile.click_profile()

        profile.wait_order_history()
        profile.perform_logout()

        assert profile.get_page_url() == Endpoints.PROFILE_PAGE