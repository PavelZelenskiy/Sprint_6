from selenium.webdriver.common.by import By

class OrderPageLocators:
   
    #order buttons
    order_button_top = [By.XPATH, "//div[contains(@class, 'Header')]//button[contains(text(), 'Заказать')]"]
    order_button_bottom = [By.XPATH, "//div[contains(@class, 'FinishButton')]//button[contains(text(), 'Заказать')]"]

    #client info page
    client_info_name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    clinet_info_surname_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    client_info_adress_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    client_info_metro_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    client_info_metro_dropdown_option = (By.XPATH, '//li[contains(@class, "select-search__row") and @data-index="0"]')
    client_info_tel_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    client_info_next_button = [By.XPATH, "//button[text()='Далее']"]

    #rent info page
    rent_info_date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rent_info_period_dropdown = [By.XPATH, "//div[text()='* Срок аренды']"]
    rent_info_period_dropdown_arrow =[By.XPATH, "//span[@class='Dropdown-arrow']"]
    rent_info_comment_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    rent_info_order_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"]

    #order confirmation modal
    order_confirm_modal_yes_button = [By.XPATH, "//button[text()='Да']"]

    #order placing modal
    order_ready_modal = [By.XPATH, "//div[text()='Заказ оформлен']"]

    #get rent info period option
    def get_rent_period_dropdown_option(period):
        return (By.XPATH, f'//div[text()="{period}"]')
    
    #get rent info color
    def get_rent_info_color(color):
        return (By.XPATH, f'//div[contains(@class,"Order_Checkboxes")]//input[@id = "{color}"]')

