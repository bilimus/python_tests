from model.contact import Contact

def test_modify_new_contact(app):
    app.contact.modify(Contact(firstname ='Bill**', middlename ='Bill**', lastname ='Imus**', \
                            nickname ='Billimus**', title = 'QA Tester**', company ='QA Solutions**', address ='Somewhere in the Universe**', \
                            home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555', \
                            email_1 ='Bill*_1@qa.com', email_2 ='Bill*_2@qa.com', email_3 ='Bill*_3@qa.com', homepage ='IhaveNoPage*.com', \
                            byear ='2000', ayear='2001', city ='Sim* City', phone2 ='+156666666', notes_here ='some notes here**'))

def test_modify_contact_firstname(app):
    app.contact.modify(Contact(firstname='Bill**'))

def test_modify_contact_middlename(app):
    app.contact.modify(Contact(middlename='Bill**'))

def test_modify_contact_lastname(app):
    app.contact.modify(Contact(lastname='Imus**'))

def test_modify_contact_nickname(app):
    app.contact.modify(Contact(nickname='Billimus**'))

def test_modify_contact_title(app):
    app.contact.modify(Contact(title='QA Tester**'))

def test_modify_contact_company(app):
    app.contact.modify(Contact(company='QA Solutions**'))

def test_modify_contact_address(app):
    app.contact.modify(Contact(address='Somewhere in the Universe**'))

def test_modify_contact_home_phone(app):
    app.contact.modify(Contact(home_phone='+13333333'))

def test_modify_contact_mobile(app):
    app.contact.modify(Contact(mobile='+122222222'))

def test_modify_contact_work_phone(app):
    app.contact.modify(Contact(work_phone='+144444444'))

def test_modify_contact_fax(app):
    app.contact.modify(Contact(fax='+155555555'))

def test_modify_contact_email_1(app):
    app.contact.modify(Contact(email_1='Bill*_1@qa.com'))

def test_modify_contact_email_2(app):
    app.contact.modify(Contact(email_2='Bill*_2@qa.com'))

def test_modify_contact_email_3(app):
    app.contact.modify(Contact(email_3='Bill*_3@qa.com'))

def test_modify_contact_homepage(app):
    app.contact.modify(Contact(homepage='IhaveNoPage*.com'))

def test_modify_contact_byear(app):
    app.contact.modify(Contact(byear='2000'))

def test_modify_contact_ayear(app):
    app.contact.modify(Contact(byear='2001'))

def test_modify_contact_city(app):
    app.contact.modify(Contact(city='Sim* City'))

def test_modify_contact_phone2(app):
    app.contact.modify(Contact(phone2='+156666666'))

def test_modify_contact_notes_here(app):
    app.contact.modify(Contact(notes_here='some notes here**'))
