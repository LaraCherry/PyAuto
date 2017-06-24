# import yaml

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = None
        self.locators = {}

    def open(self):
        self.browser.get(self.url)

    def find_element(self, name):
        #
        return self.browser.find_element_by_xpath(self.locators[name])

    def find_elements(self, name):
        # search for ALL
        return self.browser.find_elements_by_xpath(self.locators[name])
