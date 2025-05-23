Hedera:
import allure
import pytest
from pages.orders_page import OrdersPage

class TestOrders:
    @allure.title('Open order details modal')
    def test_open_order_details(self, browser, generate_user):
        orders = OrdersPage(browser)

        # Sign in and create an order
        orders.sign_in(generate_user)
        orders.click_builder()
        orders.wait_burger_area()
        orders.move_ingredient_to_burger()
        orders.click_place_order()
        orders.close_order_modal()

        # Open order details
        orders.click_orders_feed()
        orders.click_feed_order()
        assert orders.verify_order_details()

    @allure.title('History order appears in orders feed')
    def test_history_order_in_feed(self, browser, generate_user):
        orders = OrdersPage(browser)

        # Sign in and create an order
        orders.sign_in(generate_user)
        orders.click_builder()
        orders.wait_burger_area()
        orders.move_ingredient_to_burger()
        orders.click_place_order()
        order_id = orders.get_order_id()
        orders.close_order_modal()

        # Check history
        orders.click_profile()
        orders.click_order_history()
        history_order_id = orders.get_history_order_id()

        # Check feed
        orders.click_orders_feed()
        feed_order_id = orders.get_feed_order_id()
        assert order_id == history_order_id
        assert order_id == feed_order_id

    @allure.title('Total orders count increases after new order')
    def test_total_orders_count(self, browser, generate_user):
        orders = OrdersPage(browser)

        # Sign in and get initial count
        orders.sign_in(generate_user)
        orders.click_orders_feed()
        total_orders = int(orders.get_total_orders())

        # Create an order
        orders.click_builder()
        orders.wait_burger_area()
        orders.move_ingredient_to_burger()
        orders.click_place_order()
        orders.close_order_modal()

        # Get new count
        orders.click_orders_feed()
        orders.wait_for_condition(
            lambda driver: int(orders.get_total_orders()) > total_orders,
            timeout=15
        )
        total_orders_after = int(orders.get_total_orders())
        assert total_orders_after == total_orders + 1

    @allure.title('Today orders count increases after new order')
    def test_today_orders_count(self, browser, generate_user):
        orders = OrdersPage(browser)

        # Sign in and get initial count
        orders.sign_in(generate_user)
        orders.click_orders_feed()
        today_orders = int(orders.get_today_orders())

        # Create an order
        orders.click_builder()
        orders.wait_burger_area()
        orders.move_ingredient_to_burger()
        orders.click_place_order()
        orders.close_order_modal()

        # Get new count
        orders.click_orders_feed()
        orders.wait_for_condition(
            lambda driver: int(orders.get_today_orders()) > today_orders,
            timeout=15
        )
        today_orders_after = int(orders.get_today_orders())
        assert today_orders_after == today_orders + 1

    @allure.title('New order appears in in-progress section')
    def test_in_progress_order(self, browser, generate_user):
        orders = OrdersPage(browser)

        # Sign in and create an order
        orders.sign_in(generate_user)
        orders.click_builder()
        orders.wait_burger_area()
        orders.move_ingredient_to_burger()
        orders.click_place_order()
        order_id = orders.get_order_id()
        orders.close_order_modal()

        # Check in-progress section
        orders.click_orders_feed()
        in_progress_order_id = orders.get_in_progress_order_id()
        assert order_id == in_progress_order_id