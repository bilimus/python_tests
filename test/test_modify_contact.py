from model.contact import Contact
from random import randrange

def test_modify_first_contact(app):
    contacts = Contact(firstname='Bill test', middlename='Bill**', lastname='Imus**', \
            nickname='Billimus**', title='QA Tester**', company='QA Solutions**', address='Somewhere in the Universe**', \
            home_phone='+122222222', mobile='+13333333', work_phone='+14444444', fax='+15555555', \
            email_1='Bill*_1@qa.com', email_2='Bill*_2@qa.com', email_3='Bill*_3@qa.com', homepage='IhaveNoPage*.com', \
            byear='2000', ayear='2001', city='Sim* City', phone2='+156666666', notes_here='some notes here**')
    app.contact.check_presence(contacts)
    old_contacts = app.contact.get_contact_list()
    contacts.id = old_contacts[0].id
    app.contact.modify(contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_some_contact(app):
    contacts = Contact(firstname='Bill test', middlename='Bill**', lastname='Imus**', \
            nickname='Billimus**', title='QA Tester**', company='QA Solutions**', address='Somewhere in the Universe**', \
            home_phone='+122222222', mobile='+13333333', work_phone='+14444444', fax='+15555555', \
            email_1='Bill*_1@qa.com', email_2='Bill*_2@qa.com', email_3='Bill*_3@qa.com', homepage='IhaveNoPage*.com', \
            byear='2000', ayear='2001', city='Sim* City', phone2='+156666666', notes_here='some notes here**')
    app.contact.check_presence(contacts)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contacts.id = old_contacts[index].id
    app.contact.modify_contacts_by_index(index, contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

'''
def test_modify_contact_firstname(app):
    contacts = Contact(firstname='Bill test')
    app.contact.check_presence(contacts)
    old_contacts = app.contact.get_contact_list()
    contacts.id = old_contacts[0].id
    app.contact.modify(contacts)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(middlename='Bill**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(lastname='Imus**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    both_contacts = list(app.contact.compare_lists(new_contacts, old_contacts))
    assert both_contacts[0] == both_contacts[1]

def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(nickname='Billimus**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_title(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(title='QA Tester**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_company(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(company='QA Solutions**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_address(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(address='Somewhere in the Universe**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_home_phone(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(home_phone='+13333333'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_mobile(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(mobile='+122222222'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_work_phone(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(work_phone='+144444444'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_fax(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(fax='+155555555'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_email_1(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_1='Bill*_1@qa.com'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_email_2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_2='Bill*_2@qa.com'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_email_3(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_3='Bill*_3@qa.com'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_homepage(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(homepage='IhaveNoPage*.com'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_byear(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(byear='2000'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_ayear(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(byear='2001'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_city(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(city='Sim* City'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_phone2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(phone2='+156666666'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_notes_here(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(notes_here='some notes here**'))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
'''



