__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import CareersPage

class CareersPageObjects(BasePage):

    def ApplicationButton(self):
        return self.element(CareersPage.ApplicationButton)

    def click_ApplicationButton(self):
        self.element(CareersPage.ApplicationButton).click()