from Pages.PageObjectBaseClass import BaseClass

class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

email_last = "//*[@id='mesgList']/form/div[1]/a/span[3]/span"
email_before_the_last = "//*[@id='mesgList']/form/div[2]/a/span[3]/span"

