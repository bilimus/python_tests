

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change_field_value("byear", contact.byear)
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.city)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes_here)

    def modify(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_css_selector('#maintable a[href^="edit.php"]').click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()

    def open_contacts_page(self):
        wd = self.app.wd
        if not(wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_css_selector('input[value="Delete"]'))):
            wd.find_element_by_xpath('//div/div[3]/ul/li[1]/a').click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_presence(self, cnt):
        wd = self.app.wd
        if self.count() == 0:
            self.add(cnt)