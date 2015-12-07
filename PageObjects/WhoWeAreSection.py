__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import WhoWeAreSection

class WhoWeAreSectionPage(BasePage):

    def Who_We_Are_Breaker(self):
        self.element(WhoWeAreSection.Who_We_Are_Breaker)

    def Get_Who_We_Are_Breaker_position(self):
        return self.get_position(WhoWeAreSection.Who_We_Are_Breaker)
