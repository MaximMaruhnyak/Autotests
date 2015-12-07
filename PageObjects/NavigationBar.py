__author__ = 'mmaruhnyak'

from BasePage import BasePage
from Locators import NavigationBar

class NavigationBarPage(BasePage):

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