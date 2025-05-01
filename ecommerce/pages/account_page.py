from pages.base_page import BasePage



class AccountPage(BasePage):

    def get_account_page_title(self, title):
        return self.get_page_title(title)