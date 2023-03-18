from pages.po_base_class import BaseClass
from constants.locators.sent_mail_folder_page import SentMailFolderLocators


class SentMailFolder(BaseClass):

    def __init__(self,browser):
        super().__init__(browser)

    def get_sent_mail_subject(self):
        return self.get_text(SentMailFolderLocators.SENT_MAIL)

