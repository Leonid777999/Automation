from Pages.PageObjectLoginPage import LoginPage
from Pages.PageObjectMailBoxPage import MailBox
from Pages.PageObjectMailBoxPage import CurrentEmail

def test_excercise(init_browser):
    site_main_page = LoginPage(init_browser)
    mailbox_page = MailBox(init_browser)
    current_email = CurrentEmail(init_browser)

    site_main_page.enter_user_login("automate")
    site_main_page.enter_user_password("automate123")
    site_main_page.click_on_enter_button()

    assert "Осторожно мошенники!" in mailbox_page.get_email_title(mailbox_page.email_last).text
    assert "Рекомендации по безопасности Вашего аккаунта" in mailbox_page.get_email_title(mailbox_page.email_before_the_last).text

    mailbox_page.open_email(mailbox_page.email_last)

    assert "Осторожно мошенники!" in current_email.get_email_data(current_email.email_subject).text


