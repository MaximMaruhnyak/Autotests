__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import GetInTouchSection

class GetInTouchPage(BasePage):
    def Map(self):
        self.element(GetInTouchSection.Map)

    def Get_Map_position(self):
        return self.get_position(GetInTouchSection.Map)

    def LinkedIn_Icon(self):
        return self.element(GetInTouchSection.LinkedIn_Icon)

    def click_LinkedIn_Icon(self):
        self.element(GetInTouchSection.LinkedIn_Icon).click()