from selenium.webdriver.common.by import By
from Pages.PO_Login_Page import LoginPage
from Pages.PO_MailBox_Page import MailBox
from Pages.PO_MailBox_Page import CurrentEmail
from Pages.PO_New_Email_Page import New_Email
from Pages.PO_Send_Status_page import Send_status

def test_excercise(init_browser):
    site_main_page = LoginPage(init_browser)
    mailbox_page = MailBox(init_browser)
    current_email = CurrentEmail(init_browser)
    new_email = New_Email(init_browser)
    send_status = Send_status(init_browser)


    site_main_page.enter_user_login("automate")
    site_main_page.enter_user_password("automate123")
    site_main_page.click_on_enter_button()

    assert "Осторожно мошенники!" in mailbox_page.get_email_title(mailbox_page.email_first)
    assert "Рекомендации по безопасности Вашего аккаунта" in mailbox_page.get_email_title(mailbox_page.email_second)

    mailbox_page.open_email()

    assert "Осторожно мошенники!" in current_email.get_email_data(current_email.email_subject)
    assert "support@i.ua" in current_email.get_email_data(current_email.email_sender)
    assert "Automate <automate@i.ua>" in current_email.get_email_data(current_email.email_reciever)

    current_email.click_on_button(current_email.create_button)
    new_email.fill_the_field(new_email.field_to,"test@example.com")
    new_email.fill_the_field(new_email.field_text, "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    new_email.fill_the_field(new_email.field_subject, "check the mail")
    new_email.send_email(new_email.send_mail_button)
    send_status.open_sended_email_folder(send_status.sended_mails_button)

    assert "check the mail" in send_status.get_email_title(send_status.sended_mail)





