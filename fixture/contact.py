from model.contact import Contact
import re
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None
        self.open_contacts_page()

    def get_first_contact_id(self):
        self.open_contacts_page()
        wd = self.app.wd
        return wd.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')

    def delete_first_contact_from_group(self):
        wd = self.app.wd
        self.open_contacts_page()
        group_list = wd.find_elements_by_css_selector('select[name="group"] option')
        group_list[2].click()
        time.sleep(2)
        self.checked_first_contact(wd)
        time.sleep(2)
        wd.find_element_by_css_selector('input[name="remove"]').click()

        self.open_contacts_page()
        time.sleep(2)


    def add_first_contact_to_first_group(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.checked_first_contact(wd)
        self.checked_contact_added_to_first_group(wd)
        self.open_contacts_page()

    def add_contact_to_group(self,contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        box = wd.find_element_by_css_selector("select[name='to_group']")
        box.find_element_by_css_selector("option[value='%s']" % group_id).click()
        wd.find_element_by_css_selector("input[name='add']").click()
        self.app.open_home_page()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        box = wd.find_element_by_css_selector("select[name='group']")
        box.find_element_by_css_selector("option[value='%s']" % group_id).click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_css_selector("input[name='remove']").click()
        self.app.open_home_page()

    def checked_contact_added_to_first_group(self, wd):
        select_items = wd.find_elements_by_css_selector('select[name="to_group"] option')
        select_items[0].click()
        wd.find_element_by_css_selector('input[name="add"]').click()

    def checked_first_contact(self, wd):
        wd.find_element_by_css_selector('input[name="selected[]"]').click()

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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
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
        self.change_field_value("phone2", contact.secondaryphone)
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

    def modify_contacts_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id_for_editing(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_contact_by_index_for_editing(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('#maintable a[href^="edit.php"]')[index].click()

    def select_contact_by_id_for_editing(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('#maintable a[href^="edit.php?id=%s"]' % id).click()



    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        self.open_contacts_page()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("#maintable input[value='%s']" % id).click()


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

    def check_presence(self, contact):
        wd = self.app.wd
        if self.count() == 0:
            self.add(contact)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                id = element.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')
                cells = element.find_elements_by_css_selector('td')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_e_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,\
                                                  all_phones_from_home_page = all_phones, address=address,
                                                  all_e_mails_from_home_page = all_e_mails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, address=address,
                       email_1 = email_1, email_2 = email_2, email_3 = email_3 )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,\
                       workphone=workphone, secondaryphone=secondaryphone)





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