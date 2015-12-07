__author__ = 'mmaruhnyak'
from selenium import webdriver

class Environment():
    def define_environment(self, env):
        if  env == "qa":
            environment = "http://newsiteqa2.cogniance.com"
        elif env == "staging":
            environment = "http://ec2-54-157-244-22.compute-1.amazonaws.com"
        elif env == "prod":
            environment = "http://cogniance.com"
        return environment

class Browser():
    def define_browser(self, browser):
        if browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "GoogleChrome":
            driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        elif browser == "InternetExplorer":
            driver = webdriver.Ie("C:\Users\mmaruhnyak\Downloads\IEDriverServer.exe")
        return driver




