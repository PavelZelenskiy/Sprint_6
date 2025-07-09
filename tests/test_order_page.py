import pytest
import allure

from ..page_objects.order_page import OrderPage
from ..locators.order_page_locators import OrderPageLocators
from ..data import Users

@pytest.mark.usefixtures("driver_func")
class TestOrderPage:

    @classmethod
    def setup_class(cls):
        cls.driver = None

    @allure.title('Проверка работы оформления заказа')
    @allure.description('Проверка позитивного сценария оформления заказа при заполнении всех полей')

    @pytest.mark.parametrize('order_button, test_user', [
        (OrderPageLocators.order_button_top, Users.test_users[0]),
        (OrderPageLocators.order_button_bottom, Users.test_users[1])
    ])

    def test_positive_order(self, order_button, test_user):
        order_page = OrderPage(self.driver)
        order_page.scroll_to_element(order_button)
        order_page.click_element(order_button)
        order_page.filling_first_order_form(test_user)
        order_page.filling_second_order_form(test_user)
        order_page.click_confirm_modal_yes_button()
        assert order_page.check_order_ready_modal()
        
