import re

def test_phones_on_home_page(app, db):
    contacts_from_db = db.get_full_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    for contact_from_db in contacts_from_db:
        id = contact_from_db.id
        for contact_from_home_page in contacts_from_home_page:
            if contact_from_home_page.id == id:
                assert contact_from_home_page.lastname == clear(contact_from_db.lastname)
                assert contact_from_home_page.firstname == clear(contact_from_db.firstname)
                assert contact_from_home_page.address == clear(contact_from_db.address)
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_db)
'''
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    print(contact_from_view_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
'''

def clear(s):
    return re.sub(" [()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_e_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email_1, contact.email_2, contact.email_3]))))