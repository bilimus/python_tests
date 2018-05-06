from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

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

    def modify(self,contact):
        self.modify_contacts_by_index(0, contact)

    def modify_contacts_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index_for_editing(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_contact_by_index_for_editing(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('#maintable a[href^="edit.php"]')[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                id = element.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')
                box = element.find_elements_by_css_selector('td')
                firstname = box[2].text
                lastname = box[1].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

    def compare_lists(self, new_contacts, old_contacts):

        if old_contacts[0].id == new_contacts[-1].id:
            old_list = old_contacts[1:]
            new_list = new_contacts[:-1]
        elif old_contacts[0].id == new_contacts[0].id:
            old_list = old_contacts[1:]
            new_list = new_contacts[1:]
        else:
            old_list = old_contacts
            new_list = new_contacts
        return (old_list, new_list)