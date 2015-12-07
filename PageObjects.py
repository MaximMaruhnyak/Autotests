__author__ = 'mmaruhnyak'

from Locators import NavigationBar
from Locators import WhatWeDoSection
from Locators import OurWorkSection
from Locators import WhoWeAreSection
from Locators import JobSection
from Locators import GetInTouchSection
from Locators import CareersPage
from Locators import ApplyNowForm
from Locators import GoogleMail
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class BasePage(object):
    """Class that describe simple actions that we can do with our elements on the page"""

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator):
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



class MainPage(BasePage):

#Navigation bar page objects
    def Navigation_Bar(self):
        return self.element(NavigationBar.Navigation_Bar)

    def Get_Navigation_Bar_position(self):
        return self.get_position(NavigationBar.Navigation_Bar)

    def Get_Navigation_Bar_size(self):
        return self.element(NavigationBar.Navigation_Bar).size

    def click_Navigation_Bar_Logo(self):
      self.element(NavigationBar.Navigation_Bar_Logo).click()


    def What_We_Do_Menu_Item(self):
        self.element(NavigationBar.What_We_Do_Menu_Item)

    def Get_What_We_Do_Menu_Item_font(self):
        return self.get_font(NavigationBar.What_We_Do_Menu_Item)

    def Get_What_We_Do_Menu_Item_font_size(self):
        return self.get_font_size(NavigationBar.What_We_Do_Menu_Item)

    def Get_What_We_Do_Menu_Item_color(self):
        return self.get_color(NavigationBar.What_We_Do_Menu_Item)

    def Get_What_We_Do_Menu_Item_text(self):
        return self.get_text(NavigationBar.What_We_Do_Menu_Item)

    def hover_What_We_Do_Menu_Item(self):
        self.hover(NavigationBar.What_We_Do_Menu_Item)

    def click_What_We_Do_Menu_Item(self):
        self.element(NavigationBar.What_We_Do_Menu_Item).click()



    def Our_Work_Menu_Item(self):
        self.element(NavigationBar.Our_Work_Menu_Item)

    def Get_Our_Work_Menu_Item_font(self):
        return self.get_font(NavigationBar.Our_Work_Menu_Item)

    def Get_Our_Work_Menu_Item_font_size(self):
        return self.get_font_size(NavigationBar.Our_Work_Menu_Item)

    def Get_Our_Work_Menu_Item_color(self):
        return self.get_color(NavigationBar.Our_Work_Menu_Item)

    def Get_Our_Work_Menu_Item_text(self):
        return self.get_text(NavigationBar.Our_Work_Menu_Item)

    def hover_Our_Work_Menu_Item(self):
        self.hover(NavigationBar.Our_Work_Menu_Item)

    def click_Our_Work_Menu_Item(self):
        self.element(NavigationBar.Our_Work_Menu_Item).click()



    def Who_We_Are_Menu_Item(self):
        self.element(NavigationBar.Who_We_Are_Menu_Item)

    def Get_Who_We_Are_Menu_Item_font(self):
        return self.get_font(NavigationBar.Who_We_Are_Menu_Item)

    def Get_Who_We_Are_Menu_Item_font_size(self):
        return self.get_font_size(NavigationBar.Who_We_Are_Menu_Item)

    def Get_Who_We_Are_Menu_Item_color(self):
        return self.get_color(NavigationBar.Who_We_Are_Menu_Item)

    def Get_Who_We_Are_Menu_Item_text(self):
        return self.get_text(NavigationBar.Who_We_Are_Menu_Item)

    def hover_Who_We_Are_Menu_Item(self):
        self.hover(NavigationBar.Who_We_Are_Menu_Item)

    def click_Who_We_Are_Menu_Item(self):
        self.element(NavigationBar.Who_We_Are_Menu_Item).click()



    def Get_In_Touch_Menu_Item(self):
        self.element(NavigationBar.Get_In_Touch_Menu_Item)

    def Get_Get_In_Touch_Menu_Item_font(self):
        return self.get_font(NavigationBar.Get_In_Touch_Menu_Item)

    def Get_Get_In_Touch_Menu_Item_font_size(self):
        return self.get_font_size(NavigationBar.Get_In_Touch_Menu_Item)

    def Get_Get_In_Touch_Menu_Item_color(self):
        return self.get_color(NavigationBar.Get_In_Touch_Menu_Item)

    def Get_Get_In_Touch_Menu_Item_text(self):
        return self.get_text(NavigationBar.Get_In_Touch_Menu_Item)

    def hover_Get_In_Touch_Menu_Item(self):
        self.hover(NavigationBar.Get_In_Touch_Menu_Item)

    def click_Get_In_Touch_Menu_Item(self):
        self.element(NavigationBar.Get_In_Touch_Menu_Item).click()



    def Careers_Menu_Item(self):
        return self.element(NavigationBar.Careers_Menu_Item)

    def click_Careers_Menu_Item(self):
        self.element(NavigationBar.Careers_Menu_Item).click()



#What We Do page objects
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


#Our Work page objects
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


#Who We Are page objects
    def Who_We_Are_Breaker(self):
        self.element(WhoWeAreSection.Who_We_Are_Breaker)

    def Get_Who_We_Are_Breaker_position(self):
        return self.get_position(WhoWeAreSection.Who_We_Are_Breaker)


#Jobs page objects
    def Job_Breaker(self):
        return self.element(JobSection.Job_Breaker)

    def Get_Job_Breaker_position(self):
        return self.get_position(JobSection.Job_Breaker)


#Get In Touch page objects
    def Map(self):
        self.element(GetInTouchSection.Map)

    def Get_Map_position(self):
        return self.get_position(GetInTouchSection.Map)

#Media icons objects
    def LinkedIn_Icon(self):
        return self.element(GetInTouchSection.LinkedIn_Icon)

    def click_LinkedIn_Icon(self):
        self.element(GetInTouchSection.LinkedIn_Icon).click()


#Careers page objects
class CareersPageObjects(BasePage):

    def ApplicationButton(self):
        return self.element(CareersPage.ApplicationButton)

    def click_ApplicationButton(self):
        self.element(CareersPage.ApplicationButton).click()



class ApplyForm(BasePage):

    def NameField(self):
        return self.element(ApplyNowForm.NameField)

    def EmailField(self):
        return self.element(ApplyNowForm.EmailField)

    def MessageField(self):
        return self.element(ApplyNowForm.MessageField)

    def UploadButton(self):
        return self.element(ApplyNowForm.UploadButton)

    def click_UploadButton(self):
        self.element(ApplyNowForm.UploadButton).click()

    def UploadFileName(self):
        return self.element(ApplyNowForm.UploadFileName)

    def Get_UploadFileName_text(self):
        return self.get_text(ApplyNowForm.UploadFileName)

    def RemoveButton(self):
        return self.element(ApplyNowForm.RemoveButton)

    def click_RemoveButton(self):
        self.element(ApplyNowForm.RemoveButton).click()

    def ChangeButton(self):
        return self.element(ApplyNowForm.ChangeButton)

    def click_ChangeButton(self):
        self.element(ApplyNowForm.ChangeButton).click()

    def SendButton(self):
        return self.element(ApplyNowForm.SendButton)

    def click_SendButton(self):
        self.element(ApplyNowForm.SendButton).click()

    def NameFieldAlert(self):
        return self.element(ApplyNowForm.NameFieldAlert)

    def Get_NameFieldAlert_text(self):
        return self.get_text(ApplyNowForm.NameFieldAlert)

    def EmailFieldAlert(self):
        return self.element(ApplyNowForm.EmailFieldAlert)

    def Get_EmailFieldAlert(self):
        return self.get_text(ApplyNowForm.EmailFieldAlert)

    def UploadAlert(self):
        return self.element(ApplyNowForm.UploadAlert)

    def Get_UploadAlert(self):
        return self.get_text(ApplyNowForm.UploadAlert)

    def fill_Name_field(self):
        self.element(ApplyNowForm.NameField).send_keys("test")

    def fill_Email_field_correct(self):
        self.element(ApplyNowForm.EmailField).send_keys("test@gmail.com")

    def fill_Email_field_incorrect(self):
        self.element(ApplyNowForm.EmailField).send_keys("test")

    def fill_Message_field(self):
        self.element(ApplyNowForm.MessageField).send_keys("This is test CV")

    def Get_ThanksMessage_text(self):
        return self.get_text(ApplyNowForm.ThanksMessage)


class GMail(BasePage):
    def EmailField(self):
        return self.element(GoogleMail.EmailField)

    def NextButton(self):
        return self.element(GoogleMail.NextButton)

    def click_NextButton(self):
        self.element(GoogleMail.NextButton).click()

    def fill_Email_field(self):
        self.element(GoogleMail.EmailField).send_keys("")

    def PasswordField(self):
        return self.element(GoogleMail.PasswordField)

    def fill_PasswordField(self):
        self.element(GoogleMail.PasswordField).send_keys("")

    def SignInButton(self):
        return self.element(GoogleMail.SignInButton)

    def click_SignInButton(self):
        self.element(GoogleMail.SignInButton).click()

    def Sender(self):
        return self.element(GoogleMail.Sender)

    def Get_Sender_text(self):
        return self.get_text(GoogleMail.Sender)

    def Subject(self):
        return self.element(GoogleMail.Subject)

    def Get_Subject_text(self):
        return self.get_text(GoogleMail.Subject)

    def click_target_letter(self):
        self.element(GoogleMail.ListSuject).click()

    def Get_AttachmentName(self):
        return self.get_text(GoogleMail.AttachmentName)

    def click_CheckBox(self):
        self.element(GoogleMail.CheckBox).click()

    def click_ThrashButton(self):
        self.element(GoogleMail.ThrashButton).click()
















