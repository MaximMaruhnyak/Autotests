__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import GoogleMail

class GMail(BasePage):
    def EmailField(self):
        return self.element(GoogleMail.EmailField)

    def NextButton(self):
        return self.element(GoogleMail.NextButton)

    def click_NextButton(self):
        self.element(GoogleMail.NextButton).click()

    def fill_Email_field(self):
        self.element(GoogleMail.EmailField).send_keys("cgnwebtest")

    def PasswordField(self):
        return self.element(GoogleMail.PasswordField)

    def fill_PasswordField(self):
        self.element(GoogleMail.PasswordField).send_keys("f0rtest1ng")

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