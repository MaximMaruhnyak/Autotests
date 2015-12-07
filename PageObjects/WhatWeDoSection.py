__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import WhatWeDoSection

class WhatWeDoSectionPage(BasePage):

    def What_We_Do_Breaker(self):
        self.element(WhatWeDoSection.What_We_Do_Breaker)

    def Get_What_We_Do_Breaker_text(self):
        return self.get_text(WhatWeDoSection.What_We_Do_Breaker)

    def Get_What_We_Do_Breaker_font_size(self):
        return self.get_font_size(WhatWeDoSection.What_We_Do_Breaker)

    def Get_What_We_Do_Breaker_position(self):
        return self.get_position(WhatWeDoSection.What_We_Do_Breaker)


    def Strategize_Button(self):
        self.element(WhatWeDoSection.Strategize_Button)

    def hover_Strategize_Button(self):
        self.hover(WhatWeDoSection.Strategize_Button)

    def click_Strategize_Button(self):
        self.element(WhatWeDoSection.Strategize_Button).click()


    def Design_Button(self):
        self.element(WhatWeDoSection.Design_Button)

    def hover_Design_Button(self):
        self.hover(WhatWeDoSection.Design_Button)

    def click_Design_Button(self):
        self.element(WhatWeDoSection.Design_Button).click()


    def Build_Button(self):
        self.element(WhatWeDoSection.Build_Button)

    def hover_Build_Button(self):
        self.hover(WhatWeDoSection.Build_Button)

    def click_Build_Button(self):
        self.element(WhatWeDoSection.Build_Button).click()


    def Launch_Button(self):
        self.element(WhatWeDoSection.Launch_Button)

    def hover_Launch_Button(self):
        self.hover(WhatWeDoSection.Launch_Button)

    def click_Launch_Button(self):
        self.element(WhatWeDoSection.Launch_Button).click()


    def Evolve_Button(self):
        self.element(WhatWeDoSection.Evolve_Button)

    def hover_Evolve_Button(self):
        self.hover(WhatWeDoSection.Evolve_Button)

    def click_Evolve_Button(self):
        self.element(WhatWeDoSection.Evolve_Button).click()
