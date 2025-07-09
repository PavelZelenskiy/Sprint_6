import allure

from ..page_objects.base_page import BasePage
from ..locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    #FAQ section

    @allure.step('Нажатие на панель вопроса в разделе "Вопросы о важном"')
    def click_faq_heading(self, id):
        heading_locator = MainPageLocators.get_accordion_heading_locator(id)
        self.scroll_to_bottom()
        self.wait_for_element_load(heading_locator)
        self.click_element(heading_locator)

    @allure.step('Получение текста вопроса в разделе "Вопросы о важном"')
    def check_faq_heading_text(self, id):
        heading_locator = MainPageLocators.get_accordion_heading_locator(id)
        self.wait_for_element_load(heading_locator)
        return self.get_element_text(heading_locator)
    
    @allure.step('Получение текста ответа в разделе "Вопросы о важном"')
    def check_faq_panel_text(self, id):
        panel_locator = MainPageLocators.get_accordion_panel_locator(id)
        self.wait_for_element_load(panel_locator)
        return self.get_element_text(panel_locator)
    
    

        
        
        
        