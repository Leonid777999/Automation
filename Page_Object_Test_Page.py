from selenium.webdriver.common.by import By
from Pages.Page_Object_Login_Page import LoginPage
from Pages.Page_Object_MailBox_Page import MailBox
from Pages.Page_Object_MailBox_Page import CurrentEmail
from Pages.Page_Object_New_Email import New_Email

def test_excercise(init_browser):
    site_main_page = LoginPage(init_browser)
    mailbox_page = MailBox(init_browser)
    current_email = CurrentEmail(init_browser)
    new_email = New_Email(init_browser)

    site_main_page.enter_user_login("automate")
    site_main_page.enter_user_password("automate123")
    site_main_page.click_on_enter_button()

    assert "Осторожно мошенники!" in mailbox_page.get_email_title(mailbox_page.email_last)
    assert "Рекомендации по безопасности Вашего аккаунта" in mailbox_page.get_email_title(mailbox_page.email_before_the_last)

    mailbox_page.open_email()

    assert "Осторожно мошенники!" in current_email.get_email_data(current_email.email_subject)
    assert "support@i.ua" in current_email.get_email_data(current_email.email_sender)
    assert "Automate <automate@i.ua>" in current_email.get_email_data(current_email.email_reciever)

    current_email.click_on_button(current_email.create_button)
    new_email.fill_the_field(new_email.field_to,"test@example.com")
    new_email.fill_the_field(new_email.field_text, "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    new_email.fill_the_field(new_email.field_subject, "test")
    new_email.send_email(new_email.send_mail_button)
    new_email.send_email(new_email.folder_with_sended_button)



