from pages.po_login_page import LoginPage
from pages.po_mailbox_page import MailBox
from pages.po_mailbox_page import CurrentEmail
from pages.po_new_email_page import New_Email
from pages.po_send_status_page import Send_status
from app import App

def test_excercise(init_browser):
    site_main_page = LoginPage(init_browser)
    mailbox_page = MailBox(init_browser)
    current_email = CurrentEmail(init_browser)
    new_email = New_Email(init_browser)
    send_status = Send_status(init_browser)

    #login to the mailbox and get titles of two letters
    site_main_page.sign_in("automate","automate123")
    assert "Осторожно мошенники!" in mailbox_page.get_title_first_mail()
    assert "Рекомендации по безопасности Вашего аккаунта" in mailbox_page.get_title_second_mail()

    # open specific email and check the fields "subject", "from", "to"
    mailbox_page.open_email()
    assert "Осторожно мошенники!" in current_email.get_data_from_subject()
    assert "support@i.ua" in current_email.get_data_from_sender()
    assert "Automate <automate@i.ua>" in current_email.get_data_from_receiver()

    # click Create email button and switch to the creation page
    current_email.create_new_mail()

    # fill required fields and send email
    new_email.create_new_mail("test@example.com", "check the mail", "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    # open folder with the sended mails, check if the letter exists in this folder
    send_status.open_sended_mails_folder()
    assert "check the mail" in send_status.get_title_of_sended_mail()





