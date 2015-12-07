__author__ = 'mmaruhnyak'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

class BasePage(object):
    """Class that describe simple actions that we can do with our elements on the page"""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, t=5):
        t1 = 0
        while t1 < t:
            try:
                 self.driver.find_element(*locator)
                 break
            except NoSuchElementException:
                time.sleep(0.5)
                t1 += 0.5

    def element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def hover(self,locator):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*locator)).perform()

    def get_font(self, locator):
        font_family = self.element(locator).value_of_css_property("font-family")
        font_family_lower_letters = font_family.lower()
        font_family_list = font_family_lower_letters.split(",")
        return font_family_list[0]

    def get_font_size(self, locator):
        return self.element(locator).value_of_css_property("font-size")

    def get_color(self, locator):
        return self.element(locator).value_of_css_property("color")

    def get_text(self, locator):
        return self.element(locator).text

    def get_position(self, locator):
        return int(self.driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return rect.top;
        """, self.element(locator)))
