from constants import credentials


def test_exercise(app):

    # login to the mailbox and get titles of two letters
    app.login_page.sign_in(credentials.USER_LOGIN, credentials.USER_PASS)
    assert "Осторожно мошенники!" == app.mailbox_page.get_first_mail_title()
    assert "Рекомендации по безопасности Вашего аккаунта" == app.mailbox_page.get_second_mail_title()

    # get title of mails using find elements
    assert "Осторожно мошенники!" in app.mailbox_page.get_titles_by_findelements()

    # open specific email and check the fields "subject", "from", "to"
    app.mailbox_page.open_email()
    assert "Осторожно мошенники!" == app.current_email.get_email_subject()
    assert "support@i.ua" == app.current_email.get_email_sender()
    assert "Automate <automate@i.ua>" == app.current_email.get_email_receiver()

    # click Create email button and switch to the creation page
    app.current_email.goto_create_new_mail()

    # fill required fields and send email
    app.new_email.create_new_mail("test@example.com", "check the mail", "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    # open folder with the sended mails, check if the letter exists in this folder
    app.send_status.open_sent_mails_folder()
    assert "check the mail" in app.sent_mail.get_sent_mail_subject()
