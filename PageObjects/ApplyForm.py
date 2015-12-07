__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import ApplyNowForm

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

