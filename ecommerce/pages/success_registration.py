from pages.base_page import BasePage


class SuccessRegistration(BasePage):

    def get_success_register_page_title(self, title):
        return self.get_page_title(title)
