from selenium.webdriver.common.by import By

class ProfileLocators:
    PROFILE_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')
    ORDER_HISTORY_LINK = (By.XPATH, '//a[contains(text(),"История заказов")]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')