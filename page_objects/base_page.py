import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.find = self.driver.find_element
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Ожидание загрузки элемента')
    def wait_for_element_load(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание смены url')
    def wait_for_url_contains(self,url):
        self.wait.until(EC.url_contains(url))

    @allure.step('Нажатие на элемент')
    def click_element(self, locator):
        self.wait_for_element_load(locator)
        self.find(*locator).click()

    @allure.step('Получение элемента')
    def get_element(self, locator): 
        return self.find(*locator)
    
    @allure.step('Получение текста элемента')
    def get_element_text(self, locator): 
        return self.find(*locator).text
    
    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        self.wait_for_element_load(locator)
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скролл к концу страницы')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Заполнение поля')
    def send_keys(self, locator, keys):
        self.find(*locator).send_keys(keys)

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключение вкладки браузера')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    
    