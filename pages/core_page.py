from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

class CorePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def perform_click(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.browser.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait_for_visible(locator)
        return element.text

    def is_element_visible(self, locator):
        try:
            return self.wait_for_visible(locator).is_displayed()
        except:
            return False

    def verify_element_text(self, locator, expected_text):
        actual_text = self.get_element_text(locator)
        return actual_text == expected_text

    def get_current_url(self):
        return self.browser.current_url

    def drag_and_drop_element(self, source_element, target_element):
        try:
            ActionChains(self.browser).drag_and_drop(source_element, target_element).perform()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.browser.execute_script(
                "function createEvent(typeOfEvent) { "
                "var event = document.createEvent('CustomEvent'); "
                "event.initCustomEvent(typeOfEvent, true, true, null); "
                "event.dataTransfer = { "
                "data: {}, "
                "setData: function(key, value) { this.data[key] = value; }, "
                "getData: function(key) { return this.data[key]; } "
                "}; "
                "return event; "
                "} "
                "function dispatchEvent(element, typeOfEvent, event) { "
                "if (element.dispatchEvent) { "
                "element.dispatchEvent(event); "
                "} else if (element.fireEvent) { "
                "element.fireEvent('on' + typeOfEvent, event); "
                "} "
                "} "
                "function simulateHTML5DragAndDrop(element, destination) { "
                "var dragStartEvent = createEvent('dragstart'); "
                "dispatchEvent(element, 'dragstart', dragStartEvent); "
                "var dropEvent = createEvent('drop'); "
                "dispatchEvent(destination, 'drop', dropEvent); "
                "var dragEndEvent = createEvent('dragend'); "
                "dispatchEvent(element, 'dragend', dragEndEvent); "
                "} "
                "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
                source_element, target_element
            )