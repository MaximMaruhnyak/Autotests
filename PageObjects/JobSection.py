__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import JobSection

class JobSectionPage(BasePage):

    def Job_Breaker(self):
        return self.element(JobSection.Job_Breaker)

    def Get_Job_Breaker_position(self):
        return self.get_position(JobSection.Job_Breaker)