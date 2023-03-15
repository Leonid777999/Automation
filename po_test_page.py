
def test_excercise(app):

    # login to the mailbox and get titles of two letters
    app.login_page.sign_in("automate", "automate123")
    assert "Осторожно мошенники!" in app.mailbox_page.get_title_first_mail()
    assert "Рекомендации по безопасности Вашего аккаунта" in app.mailbox_page.get_title_second_mail()

    # open specific email and check the fields "subject", "from", "to"
    app.mailbox_page.open_email()
    assert "Осторожно мошенники!" in app.current_email.get_data_from_subject()
    assert "support@i.ua" in app.current_email.get_data_from_sender()
    assert "Automate <automate@i.ua>" in app.current_email.get_data_from_receiver()

    # click Create email button and switch to the creation page
    app.current_email.goto_create_new_mail()

    # fill required fields and send email
    app.new_email.create_new_mail("test@example.com", "check the mail", "texttexttexttextTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    # open folder with the sended mails, check if the letter exists in this folder
    app.send_status.open_sended_mails_folder()
    assert "check the mail" in app.send_status.get_title_of_sended_mail()
