from pages.builder_page import BuilderPage
from config import Endpoints
import allure

class TestBuilder:
    @allure.title('Navigate to builder page')
    def test_navigate_to_builder(self, browser):
        builder = BuilderPage(browser)

        builder.wait_builder_link()
        builder.click_builder()
        assert builder.get_page_url() == Endpoints.HOME_PAGE

    @allure.title('Navigate to orders feed')
    def test_navigate_to_orders_feed(self, browser):
        builder = BuilderPage(browser)

        builder.wait_builder_link()
        builder.click_orders_feed()
        assert builder.verify_orders_feed_title()

    @allure.title('Open ingredient details')
    def test_open_ingredient_details(self, browser):
        builder = BuilderPage(browser)
        builder.click_ingredient()
        assert builder.verify_ingredient_details()

    @allure.title('Close ingredient modal')
    def test_close_ingredient_modal(self, browser):
        builder = BuilderPage(browser)

        builder.click_ingredient()
        builder.wait_modal_close()
        builder.close_modal()
        assert builder.verify_modal_closed()

    @allure.title('Add bun to burger increases counter')
    def test_add_bun_to_burger(self, browser):
        builder = BuilderPage(browser)

        builder.wait_bun_item()
        builder.move_ingredient_to_burger()
        assert builder.get_ingredient_count() == '2'

    @allure.title('Place order as logged-in user')
    def test_place_order_logged_in(self, browser, generate_user):
        builder = BuilderPage(browser)

        builder.wait_builder_link()
        builder.sign_in(generate_user)

        builder.wait_bun_item()
        builder.move_ingredient_to_burger()
        builder.place_order()
        assert builder.verify_order_confirmation()