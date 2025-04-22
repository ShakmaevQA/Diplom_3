from selenium.webdriver.common.by import By

class BuilderLocators:
    BUILDER_LINK = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    ORDERS_FEED_LINK = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    ORDERS_FEED_TITLE = (By.XPATH, '//h1[contains(text(),"Лента заказов")]')
    BUN_ITEM = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    BUN_DETAILS = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')
    CLOSE_MODAL = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified__3V5XS")]')
    BURGER_DROP_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    BUN_COUNTER = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    PROFILE_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
    ORDER_CONFIRMATION = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')