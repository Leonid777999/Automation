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

    #login to the mailbox and get titles of two letters
    site_main_page.fill_the_field(site_main_page.user_login,"automate")
    site_main_page.fill_the_field(site_main_page.user_password,"automate123")
    site_main_page.click_button(site_main_page.enter_button)
    assert "Осторожно мошенники!" in mailbox_page.get_text_data(mailbox_page.email_first)
    assert "Рекомендации по безопасности Вашего аккаунта" in mailbox_page.get_text_data(mailbox_page.email_second)

    # open specific email and check the fields "subject", "from", "to"
    mailbox_page.click_button(mailbox_page.email_row_to_open)
    assert "Осторожно мошенники!" in current_email.get_text_data(current_email.email_subject)
    assert "support@i.ua" in current_email.get_text_data(current_email.email_sender)
    assert "Automate <automate@i.ua>" in current_email.get_text_data(current_email.email_reciever)

    # click Create email button and switch to the creation page
    current_email.click_button(current_email.create_button)

    # fill required filds and send email
    new_email.fill_the_field(new_email.field_to,"test@example.com")
    new_email.fill_the_field(new_email.field_text, "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    new_email.fill_the_field(new_email.field_subject, "check the mail")
    new_email.click_button(new_email.send_mail_button)

    # open folder with sended mails, check if the letter exists in this folder
    send_status.click_button(send_status.sended_mails_button)
    assert "check the mail" in send_status.get_text_data(send_status.sended_mail)





