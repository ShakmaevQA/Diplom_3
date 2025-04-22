from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    RECOVERY_LINK = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    EMAIL_INPUT = (By.CLASS_NAME, 'input__textfield')
    RECOVER_BUTTON = (By.XPATH, '//button[contains(text(),"Восстановить")]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')
    TOGGLE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//div[contains(@class, "input_status_active")]')
    PROFILE_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')