import allure
from ..page_objects.base_page import BasePage
from ..locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):  

    @allure.step('Заполнение формы "Информация о клиенте"')
    def filling_first_order_form(self, test_user):
        self.wait_for_element_load(OrderPageLocators.client_info_name_input)
        self.send_keys(OrderPageLocators.client_info_name_input, test_user['first_name'])
        self.send_keys(OrderPageLocators.clinet_info_surname_input, test_user['surname'])
        self.send_keys(OrderPageLocators.client_info_adress_input, test_user['adress'])
        self.click_element(OrderPageLocators.client_info_metro_input)
        self.send_keys(OrderPageLocators.client_info_metro_input, test_user['metro'])
        self.click_element(OrderPageLocators.client_info_metro_dropdown_option)
        self.send_keys(OrderPageLocators.client_info_tel_input, test_user['tel'])
        self.click_element(OrderPageLocators.client_info_next_button)

    @allure.step('Заполнение формы "Информация о заказе"')
    def filling_second_order_form(self, test_user):
        self.wait_for_element_load(OrderPageLocators.rent_info_date_input)
        self.click_element(OrderPageLocators.rent_info_date_input)
        self.send_keys(OrderPageLocators.rent_info_date_input, test_user['date'])
        self.click_element(OrderPageLocators.rent_info_period_dropdown_arrow)
        self.click_element(OrderPageLocators.get_rent_period_dropdown_option(test_user['rent_period']))
        self.click_element(OrderPageLocators.get_rent_info_color(test_user['color']))
        self.send_keys(OrderPageLocators.rent_info_comment_input, test_user['comment'])
        self.click_element(OrderPageLocators.rent_info_order_button)

    @allure.step('Подтверждение оформления заказа')
    def click_confirm_modal_yes_button(self):
        self.wait_for_element_load(OrderPageLocators.order_confirm_modal_yes_button)
        self.click_element(OrderPageLocators.order_confirm_modal_yes_button)

    @allure.step('Получение уведомления об оформлени заказа')
    def check_order_ready_modal(self):
        self.wait_for_element_load(OrderPageLocators.order_ready_modal)
        order_ready_modal = self.find(*OrderPageLocators.order_ready_modal)
        return order_ready_modal.is_displayed()

    

