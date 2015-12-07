__author__ = 'mmaruhnyak'

from selenium.webdriver.common.by import By

class NavigationBar(object):
    Navigation_Bar = (By.XPATH, ".//*[@id='main-menu']")
    Navigation_Bar_Logo = (By.CLASS_NAME, ".logotype.scroll-top")
    What_We_Do_Menu_Item = (By.CSS_SELECTOR, "a[data-id='what-we-do']")
    Our_Work_Menu_Item = (By.CSS_SELECTOR, "a[data-id='our-work']")
    Who_We_Are_Menu_Item = (By.CSS_SELECTOR, "a[data-id='who-we-are']")
    Get_In_Touch_Menu_Item = (By.CSS_SELECTOR, "a[data-id='get-in-touch']")
    Insights_Menu_Item = (By.XPATH, ".//*[@id='main-menu']/ul/li[5]/a")
    Careers_Menu_Item = (By.CSS_SELECTOR, "a[data-id='careers']")


class TopPicture(object):
    Top_Picture_Image = (By.CLASS_NAME, ".top-pic")


class WhatWeDoSection(object):
    What_We_Do_Breaker = (By.XPATH, ".//*[@id='what-we-do']/div[1]")
    Strategize_Button = (By.CLASS_NAME, ".step.strategize")
    Design_Button = (By.CLASS_NAME, ".step.design")
    Build_Button = (By.CLASS_NAME, ".step.build")
    Launch_Button = (By.CLASS_NAME, ".step.launch")
    Evolve_Button = (By.CLASS_NAME, ".step.evolve")


class OurWorkSection(object):
    Our_Work_Breaker = (By.XPATH, ".//*[@id='our-work']/div[1]")
    Cloud_Made_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[1]/a/img")
    Netpulse_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[2]/a/img")
    Libratone_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[3]/a/img")
    Alcohoot_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[4]/a/img")
    Expensify_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[5]/a/img")
    Tongal_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[6]/a/img")
    Beanstock_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[7]/a/img")
    Xtime_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[8]/a/img")
    Magellan_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[9]/a/img")
    Joust_Image = (By.XPATH, ".//*[@id='our-work']/ul/li[10]/a/img")
    Load_All_Button = (By.CSS_SELECTOR, ".show-dialog.open-all-projects>p")

    Cloud_Made_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[1]/a/div")
    Netpulse_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[2]/a/div")
    Libratone_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[3]/a/div")
    Alcohoot_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[4]/a/div")
    Expensify_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[5]/a/div")
    Tongal_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[6]/a/div")
    Beanstock_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[7]/a/div")
    Xtime_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[8]/a/div")
    Magellan_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[9]/a/div")
    Joust_Rollover = (By.XPATH, ".//*[@id='our-work']/ul/li[10]/a/div")





class WhoWeAreSection(object):
    Who_We_Are_Breaker = (By.XPATH, ".//*[@id='who-we-are']/div[1]")


class JobSection:
    Job_Breaker = (By.XPATH, ".//*[@id='job']/div")


class GetInTouchSection(object):
    Map = (By.CSS_SELECTOR, ".bg-map.img-responsive")
   # Silicon_Valley_Map_Item
   # New_York_Map_Item
   # London_Map_Item
   # Copenhagen_Map_Item
   # Wroclaw_Map_Item
   # Los_Angeles_Map_Item
   # Boston_Map_Item
   # Aarhus_Map_Item
   # Munich_Map_Item
   # Kyiv_Map_Item

    LinkedIn_Icon = (By.XPATH, ".//*[@id='get-in-touch']/div[2]/a[1]")
    Twitter_Icon = (By.XPATH, ".//*[@id='get-in-touch']/div[2]/a[2]")
    Facebook_Icon = (By.XPATH, ".//*[@id='get-in-touch']/div[2]/a[3]")

    # NewBusiness_Text_Item =
    # Careers_Text_Item =
    # GeneralInfo_Text_Item =

    NewBusiness_Email = (By.CSS_SELECTOR, "a[href*='mailto:newbusiness@cogniance.com']")
    Careers_Email = (By.CSS_SELECTOR, "a[href='mailto:careers@cogniance.com']")
    GeneralInfo_Email = (By.CSS_SELECTOR, "a[href='mailto:hello@cogniance.com']")


class FooterSection(object):
    Slogan = (By.CLASS_NAME, ".lead.footer")

class WPAdmin(object):
    Username = (By.XPATH, ".//*[@id='user_login']")


class CareersPage(object):
    ApplicationButton = (By.XPATH, ".//*[@id='careers-list']/div/div[2]/a")


# Locators for "Apply Now" form
class ApplyNowForm(object):

    NameField = (By.XPATH, ".//*[@id='cv_name']")
    NameFieldAlert = (By.XPATH, ".//*[@id='myModalLabel']/div/div[2]/div[1]/form/div[2]/div[1]/div")
    EmailField = (By.XPATH, ".//*[@id='cv_email']")
    EmailFieldAlert = (By.XPATH, ".//*[@id='myModalLabel']/div/div[2]/div[1]/form/div[2]/div[2]/div")
    MessageField = (By.XPATH, ".//*[@id='cv_message']")
    UploadButton = (By.XPATH, ".//*[@id='cv_file']")
    UploadAlert = (By.XPATH, ".//*[@id='myModalLabel']/div/div[2]/div[1]/form/div[2]/div[4]/div[1]")
    UploadFileName = (By.CSS_SELECTOR, "label[for=cv_file]")
    RemoveButton = (By.CSS_SELECTOR, ".file-remove")
    ChangeButton = (By.CSS_SELECTOR, ".file-change")
    SendButton = (By.CSS_SELECTOR, ".fields-container>input")
    LinkedInButton = (By.XPATH, ".//*[@id='myModalLabel']/div/div[2]/div[1]/div/div[2]")
    ThanksMessage = (By.CSS_SELECTOR, ".message-content")

class GoogleMail(object):
    EmailField = (By.CSS_SELECTOR, "#Email")
    NextButton = (By.CSS_SELECTOR, "#next")
    PasswordField = (By.CSS_SELECTOR, "#Passwd")
    SignInButton = (By.CSS_SELECTOR, "#signIn")
    Sender = (By.CSS_SELECTOR, ".gD")
    Subject = (By.CSS_SELECTOR, ".hP")
    ListSuject = (By.XPATH, ".//div[@class = 'y6']/span[contains(., 'Max')]")
    AttachmentName = (By.CSS_SELECTOR, ".aV3.a6U")
    CheckBox = (By.XPATH, ".//*[@id=':2b']/div[1]/span/div")
    ThrashButton = (By.XPATH, ".//*[@id=':5']/div/div[1]/div[1]/div/div/div[2]/div[3]")




