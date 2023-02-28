from Pages.PageObjectLoginPage import LoginPage

def test_excercise(init_browser):
    site_main_page = LoginPage(init_browser)
    site_main_page.enter_user_login("automate")


