import pytest
import allure

from ..page_objects.main_page import MainPage
from ..locators.order_page_locators import OrderPageLocators
from ..locators.main_page_locators import MainPageLocators
from ..data import MainPageFAQData
from ..urls import *


@pytest.mark.usefixtures("driver_cls")
class TestMainPage:
    
    @classmethod
    def setup_class(cls):
        cls.driver = None

    class TestFAQSection:

        @allure.title('Проверка работы раздела "Вопросы о важном"')
        @allure.description('Проверка отображения ответа при клике на вопрос и соответствия текста вопрос-ответ')

        @pytest.mark.parametrize("heading_number, heading_text, panel_number, panel_text", 
            MainPageFAQData.faq_data_combined)

        def test_faq_accordion_text(self, heading_number, panel_number, heading_text, panel_text):
            main_page = MainPage(self.driver)
            main_page.click_faq_heading(heading_number)
            assert main_page.check_faq_heading_text(heading_number) == heading_text
            assert main_page.check_faq_panel_text(panel_number) == panel_text

    class TestScooterLogoRedirect:
        
        @allure.title('Проверка работы перехода по лого "Самокат"')
        @allure.description('Проверка работы перехода на главную страницу при нажатии на лого "Самокат"')

        def test_scooter_logo_redirect(self):
            main_page = MainPage(self.driver)
            main_page.click_element(OrderPageLocators.order_button_top)
            main_page.click_element(MainPageLocators.scooter_logo)
            assert main_page.get_current_url() == BASE_URL
            
    class TestYandexLogoRedirect:
        
        @allure.title('Проверка работы перехода по лого "Яндекс"')
        @allure.description('Проверка работы перехода на главную страницу "Дзен" при нажатии на лого "Яндекс"')

        def test_scooter_logo_redirect(self):
            main_page = MainPage(self.driver)
            main_page.click_element(MainPageLocators.yandex_logo)
            main_page.switch_to_next_tab()
            main_page.wait_for_url_contains(DZEN_REDIRECT_URL)
            assert main_page.get_current_url() == DZEN_REDIRECT_URL        


        