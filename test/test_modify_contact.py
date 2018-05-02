from model.contact import Contact

def test_modify_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(firstname ='Bill**', middlename ='Bill**', lastname ='Imus**', \
                            nickname ='Billimus**', title = 'QA Tester**', company ='QA Solutions**', address ='Somewhere in the Universe**', \
                            home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555', \
                            email_1 ='Bill*_1@qa.com', email_2 ='Bill*_2@qa.com', email_3 ='Bill*_3@qa.com', homepage ='IhaveNoPage*.com', \
                            byear ='2000', ayear='2001', city ='Sim* City', phone2 ='+156666666', notes_here ='some notes here**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(firstname='Bill**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(middlename='Bill**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(lastname='Imus**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(nickname='Billimus**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_title(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(title='QA Tester**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_company(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(company='QA Solutions**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_address(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(address='Somewhere in the Universe**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_home_phone(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(home_phone='+13333333'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_mobile(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(mobile='+122222222'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_work_phone(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(work_phone='+144444444'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_fax(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(fax='+155555555'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_email_1(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_1='Bill*_1@qa.com'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_email_2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_2='Bill*_2@qa.com'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_email_3(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(email_3='Bill*_3@qa.com'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_homepage(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(homepage='IhaveNoPage*.com'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_byear(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(byear='2000'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_ayear(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(byear='2001'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_city(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(city='Sim* City'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_phone2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(phone2='+156666666'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_notes_here(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.check_presence(Contact(firstname='Bill test'))
    app.contact.modify(Contact(notes_here='some notes here**'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

