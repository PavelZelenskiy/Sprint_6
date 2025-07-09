from selenium.webdriver.common.by import By

class MainPageLocators:

    #accordion headings
    @staticmethod
    def get_accordion_heading_locator(heading_id):
        return By.ID, f'accordion__heading-{heading_id}'
   
    #accordion panels
    @staticmethod
    def get_accordion_panel_locator(panel_id):
        return By.ID, f'accordion__panel-{panel_id}'

    #Yandex logo
    yandex_logo = [By.XPATH, "//a[@href='//yandex.ru']"]

    #scooter logo
    scooter_logo = [By.XPATH, "//a[@href='/']"]

    
    
    

