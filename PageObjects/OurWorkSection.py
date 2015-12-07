__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import OurWorkSection

class OurWorkSectionPage(BasePage):
    def Our_Work_Breaker(self):
        self.element(OurWorkSection.Our_Work_Breaker)

    def Get_Our_Work_Breaker_position(self):
        return self.get_position(OurWorkSection.Our_Work_Breaker)


    def Cloud_Made_Image(self):
        self.element(OurWorkSection.Cloud_Made_Image)

    def hover_Cloud_Made_Image(self):
        self.hover(OurWorkSection.Cloud_Made_Image)

    def click_Cloud_Made_Image(self):
        self.element(OurWorkSection.Cloud_Made_Image).click()


    def Netpulse_Image(self):
        self.element(OurWorkSection.Netpulse_Image)

    def hover_Netpulse_Image(self):
        self.hover(OurWorkSection.Netpulse_Image)

    def click_Netpulse_Image(self):
        self.element(OurWorkSection.Netpulse_Image).click()


    def Libratone_Image(self):
        self.element(OurWorkSection.Libratone_Image)

    def hover_Libratone_Image(self):
        self.hover(OurWorkSection.Libratone_Image)

    def click_Libratone_Image(self):
        self.element(OurWorkSection.Libratone_Image).click()


    def Alcohoot_Image(self):
        self.element(OurWorkSection.Alcohoot_Image)

    def hover_Alcohoot_Image(self):
        self.hover(OurWorkSection.Alcohoot_Image)

    def click_Alcohoot_Image(self):
        self.element(OurWorkSection.Alcohoot_Image).click()


    def Expensify_Image(self):
        self.element(OurWorkSection.Expensify_Image)

    def hover_Expensify_Image(self):
        self.hover(OurWorkSection.Expensify_Image)

    def click_Expensify_Image(self):
        self.element(OurWorkSection.Expensify_Image).click()


    def Tongal_Image(self):
        self.element(OurWorkSection.Tongal_Image)

    def hover_Tongal_Image(self):
        self.hover(OurWorkSection.Tongal_Image)

    def click_Tongal_Image(self):
        self.element(OurWorkSection.Tongal_Image).click()


    def Beanstock_Image(self):
        self.element(OurWorkSection.Beanstock_Image)

    def hover_Beanstock_Image(self):
        self.hover(OurWorkSection.Beanstock_Image)

    def click_Beanstock_Image(self):
        self.element(OurWorkSection.Beanstock_Image).click()


    def Xtime_Image(self):
        self.element(OurWorkSection.Xtime_Image)

    def hover_Xtime_Image(self):
        self.hover(OurWorkSection.Xtime_Image)

    def click_Xtime_Image(self):
        self.element(OurWorkSection.Xtime_Image).click()


    def Magellan_Image(self):
        self.element(OurWorkSection.Magellan_Image)

    def hover_Magellan_Image(self):
        self.hover(OurWorkSection.Magellan_Image)

    def click_Magellan_Image(self):
        self.element(OurWorkSection.Magellan_Image).click()


    def Joust_Image(self):
        self.element(OurWorkSection.Joust_Image)

    def hover_Joust_Image(self):
        self.hover(OurWorkSection.Joust_Image)

    def click_Joust_Image(self):
        self.element(OurWorkSection.Joust_Image).click()


    def Cloud_Made_Rollover(self):
        return self.element(OurWorkSection.Cloud_Made_Rollover)

    def Get_Cloud_Made_Rollover_text(self):
        return self.get_text(OurWorkSection.Cloud_Made_Rollover)


    def Netpulse_Rollover(self):
        return self.element(OurWorkSection.Netpulse_Rollover)

    def Get_Netpulse_Rollover_text(self):
        return self.get_text(OurWorkSection.Netpulse_Rollover)


    def Libratone_Rollover(self):
        return self.element(OurWorkSection.Libratone_Rollover)

    def Get_Libratone_Rollover_text(self):
        return self.get_text(OurWorkSection.Libratone_Rollover)


    def Alcohoot_Rollover(self):
        return self.element(OurWorkSection.Alcohoot_Rollover)

    def Get_Alcohoot_Rollover_text(self):
        return self.get_text(OurWorkSection.Alcohoot_Rollover)


    def Expensify_Rollover(self):
        return self.element(OurWorkSection.Expensify_Rollover)

    def Get_Expensify_Rollover_text(self):
        return self.get_text(OurWorkSection.Expensify_Rollover)


    def Tongal_Rollover(self):
        return self.element(OurWorkSection.Tongal_Rollover)

    def Get_Tongal_Rollover_text(self):
        return self.get_text(OurWorkSection.Tongal_Rollover)


    def Beanstock_Rollover(self):
        return self.element(OurWorkSection.Beanstock_Rollover)

    def Get_Beanstock_Rollover(self):
        return self.get_text(OurWorkSection.Beanstock_Rollover)


    def Xtime_Rollover(self):
        return self.element(OurWorkSection.Xtime_Rollover)

    def Get_Xtime_Rollover_text(self):
        return self.get_text(OurWorkSection.Xtime_Rollover)


    def Magellan_Rollover(self):
        return self.element(OurWorkSection.Magellan_Rollover)

    def Get_Magellan_Rollover_text(self):
        return self.get_text(OurWorkSection.Magellan_Rollover)


    def Joust_Rollover(self):
        return self.element(OurWorkSection.Joust_Rollover)

    def Get_Joust_Rollover_text(self):
        return self.get_text(OurWorkSection.Joust_Rollover)


    def Load_All_Button(self):
        self.element(OurWorkSection.Load_All_Button)

    def size_Load_All_Button(self):
        return self.element(OurWorkSection.Load_All_Button).get_attribute("style")

    def hover_Load_All_Button(self):
        self.hover(OurWorkSection.Load_All_Button)

    def click_Load_All_Button(self):
       self.element(OurWorkSection.Load_All_Button).click()
