__author__ = 'mmaruhnyak'

import time
import pytest
import PageObjects
import sys
import os
from Config import Environment
from Config import Browser
from selenium import webdriver


# class TestMainPage():
#
#     @classmethod
#     def setup_class(self):
#         self.driver = Browser().define_browser(sys.argv[2])
#         self.driver.maximize_window()
#         self.main_page = PageObjects.MainPage(self.driver)
#         self.careers_page = PageObjects.CareersPageObjects(self.driver)
#         self.mail_page = PageObjects.GMail(self.driver)
#
#     @classmethod
#     def teardown_class(self):
#         self.driver.quit()
#
#     def setup_method(self, method):
#         self.driver.get(Environment().define_environment(sys.argv[1]))  #Need to change the call of environment variable
#
#
#     def teardown_method(self, method):
#         print ("End of test case")
#
#
    # #Test cases
    #
    # #Check if the title of website is correct
    # def test_title(self):
    #     assert self.driver.title == 'Cogniance ' + u"\u2014 " + 'Your Intelligence. Multiplied.'
    #
    # #Check if description of website is correct
    # def test_description(self):
    #     assert self.driver.find_element_by_xpath("//meta[@name='description']").get_attribute(
    #         "content") == 'Cogniance is a global organization with roots in Silicon Valley. We exist to help innovators bring software and hardware innovations to market. In essence, we co-create technology products.'
    #
    # def test_Navigation_Bar_dimensions(self):
    #     assert self.main_page.Get_Navigation_Bar_size() == {'width': 1200, 'height': 80}
    #
    # def test_Navigation_Bar_position(self):
    #     assert self.main_page.Get_Navigation_Bar_position() == 50
    #
    #
    # #Check if the text of menu items is correct
    # def test_What_We_Do_text(self):
    #     assert self.main_page.Get_What_We_Do_Menu_Item_text() == 'What We Do'
    #
    # def test_Our_Work_text(self):
    #     assert self.main_page.Get_Our_Work_Menu_Item_text() == 'Our Work'
    #
    # def test_Who_We_Are_text(self):
    #     assert self.main_page.Get_Who_We_Are_Menu_Item_text() == 'Who We Are'
    #
    # def test_Get_In_Touch(self):
    #     assert self.main_page.Get_Get_In_Touch_Menu_Item_text() == 'Get In Touch'
    #
    #
    # #Check if the text of menu items has correct font
    # def test_What_We_Do_Menu_Item_font(self):
    #     assert self.main_page.Get_What_We_Do_Menu_Item_font() == "signawebpro-extlight"
    #
    # def test_Our_Work_Item_font(self):
    #     assert self.main_page.Get_Our_Work_Menu_Item_font() == "signawebpro-extlight"
    #
    # def test_Who_We_Are_Item_font(self):
    #     assert self.main_page.Get_Who_We_Are_Menu_Item_font() == "signawebpro-extlight"
    #
    # def test_Get_In_Touch_Item_font(self):
    #     assert self.main_page.Get_Get_In_Touch_Menu_Item_font() == "signawebpro-extlight"
    #
    #
    # #Check if the text of menu items has correct size
    # def test_What_We_Do_Menu_Item_font_size(self):
    #     assert self.main_page.Get_What_We_Do_Menu_Item_font_size() == "20px"
    #
    # def test_Our_Work_Menu_Item_font_size(self):
    #     assert self.main_page.Get_Our_Work_Menu_Item_font_size() == "20px"
    #
    # def test_Who_We_Are_Menu_Item_font_size(self):
    #     assert self.main_page.Get_Who_We_Are_Menu_Item_font_size() == "20px"
    #
    # def test_Get_In_Touch_Menu_Item_font_size(self):
    #     assert self.main_page.Get_Get_In_Touch_Menu_Item_font_size() == "20px"
    #
    #     #   def test_What_We_Do_Menu_Item_color(self):
    #     #       assert self.main_page.Get_What_We_Do_Menu_Item_color() == "#666"
    #
    #
    # #Check if the URL is correct after clicking menu items in nav bar
    # def test_What_We_Do_URL(self):
    #     self.main_page.click_What_We_Do_Menu_Item()
    #     assert self.driver.current_url == '%s/#what-we-do' % Environment().define_environment(
    #         sys.argv[1])  #Need to change the call of environment variable
    #
    # def test_Our_Work_URL(self):
    #     self.main_page.click_Our_Work_Menu_Item()
    #     assert self.driver.current_url == '%s/#our-work' % Environment().define_environment(
    #         sys.argv[1])  #Need to change the call of environment variable
    #
    # def test_Who_We_Are_URL(self):
    #     self.main_page.click_Who_We_Are_Menu_Item()
    #     assert self.driver.current_url == '%s/#who-we-are' % Environment().define_environment(
    #         sys.argv[1])  #Need to change the call of environment variable
    #
    # def test_Get_In_Touch_URL(self):
    #     self.main_page.click_Get_In_Touch_Menu_Item()
    #     assert self.driver.current_url == '%s/#get-in-touch' % Environment().define_environment(
    #         sys.argv[1])  #Need to change the call of environment variable
    #
    # #Check if the anchor point is correct after click on menu items in nav bar
    #
    # def test_What_We_Do_anchor(self):
    #     assert self.main_page.Get_What_We_Do_Breaker_position() == 79
    #     self.main_page.click_Careers_Menu_Item()
    #     time.sleep(2)
    #     self.careers.click_ApplicationButton()
    #     time.sleep(5)
    #
    # def test_Our_Work_anchor(self):
    #     self.main_page.click_Our_Work_Menu_Item()
    #     time.sleep(1)
    #     assert self.main_page.Get_Our_Work_Breaker_position() == 79
    #
    # def test_Who_We_Are_anchor(self):
    #     self.main_page.click_Who_We_Are_Menu_Item()
    #     time.sleep(1)
    #     assert self.main_page.Get_Who_We_Are_Breaker_position() == 79
    #
    # def test_Get_In_Touch_anchor(self):
    #     self.main_page.click_Get_In_Touch_Menu_Item()
    #     time.sleep(1)
    #     assert self.main_page.Get_Map_position() == 79
    #
    # #Check if Case study rollovers appears on hover
    # def test_Cloud_Made_Rollover_appearance(self):
    #     self.main_page.hover_Cloud_Made_Image()
    #     time.sleep(1)
    #     assert self.main_page.Cloud_Made_Rollover().is_displayed()
    #
    # def test_Netpulse_Rollover_appearance(self):
    #     self.main_page.hover_Netpulse_Image()
    #     time.sleep(1)
    #     assert self.main_page.Netpulse_Rollover().is_displayed()
    #
    # def test_Libratone_Rollover_appearance(self):
    #     self.main_page.hover_Libratone_Image()
    #     time.sleep(1)
    #     assert self.main_page.Libratone_Rollover().is_displayed()
    #
    # def test_Alcohoot_Rollover_appearance(self):
    #     self.main_page.hover_Alcohoot_Image()
    #     time.sleep(1)
    #     assert self.main_page.Alcohoot_Rollover().is_displayed()
    #
    # def test_Expensify_Rollover_appearance(self):
    #     self.main_page.hover_Expensify_Image()
    #     time.sleep(1)
    #     assert self.main_page.Expensify_Rollover().is_displayed()
    #
    # def test_Tongal_Rollover_appearance(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Tongal_Image()
    #     time.sleep(1)
    #     assert self.main_page.Tongal_Rollover().is_displayed()
    #
    # def test_Beanstock_Rollover_appearance(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Beanstock_Image()
    #     time.sleep(1)
    #     assert self.main_page.Beanstock_Rollover().is_displayed()
    #
    # def test_Xtime_Rollover_appearance(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Xtime_Image()
    #     time.sleep(1)
    #     assert self.main_page.Xtime_Rollover().is_displayed()
    #
    # def test_Magellan_Rollover_appearance(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Magellan_Image()
    #     time.sleep(1)
    #     assert self.main_page.Magellan_Rollover().is_displayed()
    #
    # def test_Joust_Rollover_appearance(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Joust_Image()
    #     time.sleep(1)
    #     assert self.main_page.Joust_Rollover().is_displayed()
    #
    #
    # #Check if the text in Case study rollovers is correct
    # def test_Cloud_Made_Rollover_text(self):
    #     self.main_page.hover_Cloud_Made_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Cloud_Made_Rollover_text() == "Connected Car Solutions"
    #
    # def test_Netpulse_Rollover_text(self):
    #     self.main_page.hover_Netpulse_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Netpulse_Rollover_text() == "Digital Fitness Platform"
    #
    # def test_Libratone_Rollover_text(self):
    #     self.main_page.hover_Libratone_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Libratone_Rollover_text() == "Award-Winning Wireless Speakers"
    #
    # def test_Aloohoot_Rollover_text(self):
    #     self.main_page.hover_Alcohoot_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Alcohoot_Rollover_text() == "Smartphone Breathalyzer"
    #
    # def test_Expensify_Rollover_text(self):
    #     self.main_page.hover_Expensify_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Expensify_Rollover_text() == "Expense Reporting Made Easy"
    #
    # def test_Tongal_Rollover_text(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Tongal_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Tongal_Rollover_text() == "Creativity Set Free"
    #
    # def test_Beanstock_Rollover_text(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Beanstock_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Beanstock_Rollover() == "Publisher Trading Desk"
    #
    # def test_Xtime_Rollover_text(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Xtime_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Xtime_Rollover_text() == "Dealer Management System"
    #
    # def test_Magellan_Rollover_text(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Magellan_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Magellan_Rollover_text() == "Cloud-Enabled SmartGPS"
    #
    # def test_Joust_Rollover_text(self):
    #     self.main_page.click_Load_All_Button()
    #     self.main_page.hover_Joust_Image()
    #     time.sleep(1)
    #     assert self.main_page.Get_Joust_Rollover_text() == "Real-Time Gamification Platform"
    #
    #
    # #Check if the size of "Load All" text is correct
    # def test_Load_All_font_size(self):
    #     assert self.main_page.size_Load_All_Button() == "font-size: 21px;"
    #
    #
    #
    # #Check if the text in breakers is correct
    # def test_What_We_Do_Breaker_text(self):
    #    assert self.main_page.Get_What_We_Do_Breaker_text() == "Pragmatic Co-Creation. From inception to launch and beyond,\nwe help innovators bring technology products to market"

class TestApplyNowForm():

    @classmethod
    def setup_class(self):
        self.driver = Browser().define_browser(sys.argv[2])
        self.driver.maximize_window()

    @classmethod
    def teardown_class(self):
        self.driver.quit()

    def setup_method(self, method):
        self.driver.get('%s/careers/#job/boston/python-engineer' % Environment().define_environment(sys.argv[1])) #Need to change the call of environment variable
        self.driver.refresh()
        self.apply_form = PageObjects.ApplyForm(self.driver)
        self.mail_page = PageObjects.GMail(self.driver)

    def teardown_method(self, method):
        print ("End of test case")


    def Exception(self):
        Counter = 0
        while t1 < 30:
            t1 = 0
            try:
                element = self.driver.find_element_by_css_selector()
                break
            except NoSuchElementException:
                Counter += 0.5

    # #Test Apply form alerts
    # def test_empty_Apply_Form(self):
    #     self.apply_form.click_SendButton()
    #     time.sleep(2)
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == "Email address is required"
    #     assert self.apply_form.Get_UploadAlert() == "Please attach CV"
    #
    # def test_Apply_Form_filled_Name(self):
    #     self.apply_form.fill_Name_field()
    #     self.apply_form.click_SendButton()
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == ""
    #     assert self.apply_form.Get_EmailFieldAlert() == "Email address is required"
    #     assert self.apply_form.Get_UploadAlert() == "Please attach CV"
    #
    # def test_Apply_Form_filled_Email_incorrect(self):
    #     self.apply_form.fill_Email_field_incorrect()
    #     self.apply_form.click_SendButton()
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == "Given email address is not valid"
    #     assert self.apply_form.Get_UploadAlert() == "Please attach CV"
    #
    # def test_Apply_Form_filled_Email_correct(self):
    #     self.apply_form.fill_Email_field_correct()
    #     self.apply_form.click_SendButton()
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == ""
    #     assert self.apply_form.Get_UploadAlert() == "Please attach CV"
    #
    # def test_Upload_correct_file(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
    #     self.apply_form.click_SendButton()
    #     time.sleep(1)
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == "Email address is required"
    #     assert self.apply_form.Get_UploadAlert() == ""
    #
    # def test_Upload_oversized_file(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\OversizedTestCV.exe")
    #     self.apply_form.click_SendButton()
    #     time.sleep(1)
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == "Email address is required"
    #     assert self.apply_form.Get_UploadAlert() == "File size exceeded 3 Mb"
    #
    # def test_Upload_incorrect_format_file(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\IncorrectFormat.exe")
    #     self.apply_form.click_SendButton()
    #     time.sleep(1)
    #
    #     assert self.apply_form.Get_NameFieldAlert_text() == "Name field is required"
    #     assert self.apply_form.Get_EmailFieldAlert() == "Email address is required"
    #     assert self.apply_form.Get_UploadAlert() == "Only doc, pdf, ppt allowed"
    #
    # def test_aditional_buttons(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
    #     self.apply_form.click_SendButton()
    #     time.sleep(1)
    #
    #     assert self.apply_form.Get_UploadFileName_text() == "TestCV.doc"
    #     assert self.apply_form.RemoveButton().is_displayed()
    #     assert self.apply_form.ChangeButton().is_displayed()
    #
    # def test_Remove_button(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
    #     self.apply_form.click_RemoveButton()
    #     self.apply_form.click_SendButton()
    #
    #     assert self.apply_form.Get_UploadAlert() == "Please attach CV"
    #
    #
    #

    # def test_Change_button(self):
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
    #     time.sleep(1)
    #     assert self.apply_form.Get_UploadFileName_text() == "TestCV.doc"
    #     time.sleep(1)
    #     self.apply_form.click_ChangeButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\OversizedTestCV.exe") #Need to find solution how to rewrite text of file name
    #     time.sleep(1)
    #
    #     assert self.apply_form.Get_UploadFileName_text() == "OversizedTestCV.doc"
    #
    # def test_thanks_message(self):
    #     self.apply_form.fill_Name_field()
    #     self.apply_form.fill_Email_field_correct()
    #     time.sleep(3)
    #     self.apply_form.click_UploadButton()
    #     os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
    #     time.sleep(3)
    #     self.apply_form.click_SendButton()
    #
    #     assert self.apply_form.Get_ThanksMessage_text() == "Thanks for applying. We" + u"\u2019" + "ll get in touch soon."

    def test_mail_received(self):
        self.driver.get("https://mail.google.com/mail/u/1/?tab=wm#inbox")
        time.sleep(2)
        self.mail_page.fill_Email_field()
        self.mail_page.click_NextButton()
        time.sleep(1)
        self.mail_page.fill_PasswordField()
        self.mail_page.click_SignInButton()
        time.sleep(5)
        self.mail_page.click_CheckBox()
        self.mail_page.click_ThrashButton()
        time.sleep(5)

        self.driver.get('%s/careers/#job/boston/python-engineer' % Environment().define_environment(sys.argv[1]))
        self.apply_form.fill_Name_field()
        self.apply_form.fill_Email_field_correct()
        time.sleep(3)
        self.apply_form.click_UploadButton()
        os.system("C:\Users\mmaruhnyak\Desktop\TestCV.exe")
        time.sleep(3)
        self.apply_form.click_SendButton()

        self.driver.get("https://mail.google.com/mail/u/1/?tab=wm#inbox")
        time.sleep(2)
        self.mail_page.fill_Email_field()
        self.mail_page.click_NextButton()
        time.sleep(1)
        self.mail_page.fill_PasswordField()
        self.mail_page.click_SignInButton()
        time.sleep(5)
        self.mail_page.click_target_letter()
        time.sleep(2)


        assert self.mail_page.Get_Sender_text() == "test"
        assert self.mail_page.Get_Subject_text() == "[CV][Python Engineer][Boston, MA] test"
        assert self.mail_page.Get_AttachmentName() == "TestCV.doc"


if __name__ == '__main__':
    pytest.main([__file__, '-v', "--capture=sys", "--junitxml=results.xml"])
